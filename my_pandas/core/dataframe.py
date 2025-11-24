from .groupby import GroupBy
class DataFrame:
    def __init__(self, data: dict):
        self.data = data
        self.columns = list(data.keys())
        self.length = len(next(iter(data.values()))) if data else 0

    def __repr__(self):
        return f"DataFrame({self.data})"

    def __getitem__(self, key):
        if isinstance(key, str):
            return DataFrame({key: self.data[key]}) 
        
        if isinstance(key, list) and all(isinstance(x, bool) for x in key):
            new_data = {}
            for col, values in self.data.items():
                new_data[col] = [v for v, keep in zip(values, key) if keep]
            return DataFrame(new_data)                     
        
        if isinstance(key, list):                       
            subset = {col: self.data[col] for col in key}
            return DataFrame(subset)
    
    def head(self, n=5):
        n = min(n, self.length)
        new_data = {col: self.data[col][:n] for col in self.data}
        return DataFrame(new_data)
    
    def unique(self, column):
        return list(set(self.data[column]))
    
    def isin(self, column, values):
        col = self.data[column]
        return [v in values for v in col]
    
    def copy(self):
        new_data = {col: values.copy() for col, values in self.data.items()}
        return DataFrame(new_data)
    
    def groupby(self, column):
        return GroupBy(self, column)
    
    def merge(self, right, left_on, right_on, how="inner"):
        result_data = {}
        
        right_map = {}
        for r_val, idx in zip(right.data[right_on], range(right.length)):
            if r_val not in right_map:
                right_map[r_val] = []
            right_map[r_val].append(idx)

        merged_rows = []
        for i, l_val in enumerate(self.data[left_on]):
            right_indices = right_map.get(l_val, [])
            
            if right_indices:
                for r_idx in right_indices:
                    row = {}
                    for col in self.columns:
                        row[col] = self.data[col][i]
                    for col in right.columns:
                        if col != right_on:
                            row[col] = right.data[col][r_idx]
                    merged_rows.append(row)
            elif how in ("left", "outer"):
                row = {}
                for col in self.columns:
                    row[col] = self.data[col][i]
                for col in right.columns:
                    if col != right_on:
                        row[col] = None
                merged_rows.append(row)

        if how in ("right", "outer"):
            left_vals = set(self.data[left_on])
            for r_idx, r_val in enumerate(right.data[right_on]):
                if r_val not in left_vals:
                    row = {}
                    for col in self.columns:
                        row[col] = None
                    for col in right.columns:
                        if col != right_on:
                            row[col] = right.data[col][r_idx]
                    merged_rows.append(row)

        merged_data = {col: [] for col in merged_rows[0]} if merged_rows else {}
        for row in merged_rows:
            for col, val in row.items():
                merged_data[col].append(val)

        return DataFrame(merged_data)
    
    def sort_values(self, by, ascending=True):
        col = self.data[by]
        sorted_indices = sorted(range(self.length), key=lambda i: col[i], reverse=not ascending)
        new_data = {}
        for c in self.columns:
            new_data[c] = [self.data[c][i] for i in sorted_indices]
        
        return DataFrame(new_data)
    
    def rename(self, columns):
        new_data = {}
        for col, values in self.data.items():
            new_col = columns.get(col, col)
            new_data[new_col] = values
        return DataFrame(new_data)