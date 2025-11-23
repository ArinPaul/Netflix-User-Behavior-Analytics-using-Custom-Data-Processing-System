from .groupby import GroupBy
class DataFrame:
    def __init__(self, data: dict):
        self.data = data
        self.columns = list(data.keys())
        self.length = len(next(iter(data.values()))) if data else 0

    def __getitem__(self, key):
        if isinstance(key, str):
            return DataFrame({key: self.data[key]})                      
        
        if isinstance(key, list):                       
            subset = {col: self.data[col] for col in key}
            return DataFrame(subset)
        
        if isinstance(key, list) and all(isinstance(x, bool) for x in key):
            new_data = {}
            for col, values in self.data.items():
                new_data[col] = [v for v, keep in zip(values, key) if keep]
            return DataFrame(new_data)
    
    def head(self, n=5):
        num_rows = self.length
        for i in range(min(n, num_rows)):
            row = {col: self.data[col][i] for col in self.data}
            print(row)
    
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
    