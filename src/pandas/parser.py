def custom_read_csv(file_path, delimiter):
    data = []
    with open(file_path, 'r') as file:
        headers = file.readline().strip().split(delimiter)
        for line in file:
            values = line.strip().split(delimiter)
            row = {headers[i]: values[i] for i in range(len(headers))}
            data.append(row)
    return data


# Need to handle type conversion and missing values
# Need to handle , and " in the data