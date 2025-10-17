class Series:
    def __init__(self, data):
        self.data = data
        self.dtype = type(data[0]).__name__ if data else None

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return "\n".join([str(x) for x in self.data])
