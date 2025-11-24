class GroupBy:
    def __init__(self, df, by):
        self.df = df
        self.by = by

        self.groups = {}
        col_values = df.data[by]

        for i, key in enumerate(col_values):
            if key not in self.groups:
                self.groups[key] = []
            self.groups[key].append(i)

    def agg(self, agg_dict):
        from .dataframe import DataFrame
        result = {self.by: []}

        for col, funcs in agg_dict.items():
            if isinstance(funcs, str):
                result[f"{col}_{funcs}"] = []
            else:
                for f in funcs:
                    result[f"{col}_{f}"] = []

        for group_key, row_indices in self.groups.items():
            result[self.by].append(group_key)

            for col, funcs in agg_dict.items():
                values = [self.df.data[col][i] for i in row_indices]

                if isinstance(funcs, str):
                    funcs = [funcs]

                for f in funcs:
                    if f == "sum":
                        val = sum(values)
                    elif f == "count":
                        val = len(values)
                    elif f == "avg":
                        val = sum(values) / len(values)
                    elif f == "min":
                        val = min(values)
                    elif f == "max":
                        val = max(values)
                    else:
                        raise ValueError("Unknown aggregation: " + f)

                    result[f"{col}_{f}"].append(val)

        return DataFrame(result)

