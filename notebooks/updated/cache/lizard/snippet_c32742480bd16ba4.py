def build_dummies_dict(data):
    unique_val_list = unique(data)
    output = {}
    for val in unique_val_list:
        output[val] = data == val
    return output