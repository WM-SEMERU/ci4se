def load(data_path):
    with open(data_path, 'r') as data_file:
        raw_data = data_file.read()
    data_file.close()
    return raw_data