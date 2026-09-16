def calculate_size(name, value):
    data_size = 0
    data_size += calculate_size_str(name)
    data_size += calculate_size_data(value)
    return data_size