def data_columns_to_dict(columns_string, dict_string, delimiter=None):
    if delimiter:
        return {k: v for k, v in zip(columns_string.split(delimiter),
            dict_string.split(delimiter))}
    else:
        return {k: v for k, v in zip(columns_string.split(), dict_string.
            split())}