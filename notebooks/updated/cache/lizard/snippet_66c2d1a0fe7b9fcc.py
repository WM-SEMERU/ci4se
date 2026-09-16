def _many_to_one(input_dict):
    return dict((key, val) for keys, val in input_dict.items() for key in keys)