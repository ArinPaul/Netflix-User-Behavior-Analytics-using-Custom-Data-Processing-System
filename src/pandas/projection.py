def custom_projection(data, columns):
    __getitem__ = lambda obj, key: obj[key] if isinstance(obj, dict) else getattr(obj, key, None)
    projected_data = []
    for row in data:
        projected_row = {col: __getitem__(row, col) for col in columns}
        projected_data.append(projected_row)
    return projected_data       