from .series import Series
class DataFrame:
    def __init__(self, data):
        """
        Initialize DataFrame from dict of lists or dict of Series.
        Example:
            df = DataFrame({'A': [1,2], 'B':[3,4]})
        """
        self.data = {k: Series(v) for k, v in data.items()}
        self.columns = list(self.data.keys())
        self.nrows = len(next(iter(self.data.values())).data)

    def __getitem__(self, key):
        """Allow df['col'] access."""
        if isinstance(key, list):
            return DataFrame({k: self.data[k].data for k in key})
        return self.data[key]

    def __setitem__(self, key, value):
        """Allow df['col'] = ..."""
        if len(value) != self.nrows:
            raise ValueError("Column length must match number of rows.")
        self.data[key] = Series(value)
        if key not in self.columns:
            self.columns.append(key)

    def __repr__(self):
        rows = []
        for i in range(self.nrows):
            row = [str(self.data[c].data[i]) for c in self.columns]
            rows.append("\t".join(row))
        return f"{' | '.join(self.columns)}\n" + "\n".join(rows)

    # --- Pandas-like methods ---
    def head(self, n=5):
        """Return first n rows."""
        data = {c: s.data[:n] for c, s in self.data.items()}
        return DataFrame(data)

    def tail(self, n=5):
        """Return last n rows."""
        data = {c: s.data[-n:] for c, s in self.data.items()}
        return DataFrame(data)

    def shape(self):
        return (self.nrows, len(self.columns))
