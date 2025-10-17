from ..core.dataframe import DataFrame

def read_csv(filename, delimiter=','):
    with open(filename, 'r') as f:
        lines = f.read().strip().split('\n')

    header = lines[0].split(delimiter)
    data = {h: [] for h in header}

    for line in lines[1:]:
        values = line.split(delimiter)
        for h, v in zip(header, values):
            val = v.strip()
            if val.replace('.', '', 1).isdigit():
                val = float(val) if '.' in val else int(val)
            data[h].append(val)

    return DataFrame(data)
