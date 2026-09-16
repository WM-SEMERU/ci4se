def user_loc_value_to_instance_string(axis_tag, user_loc):
    codes = {}
    if axis_tag == 'wght':
        codes = WEIGHT_CODES
    elif axis_tag == 'wdth':
        codes = WIDTH_CODES
    else:
        raise NotImplementedError
    class_ = user_loc_value_to_class(axis_tag, user_loc)
    return min(sorted((code, class_) for code, class_ in codes.items() if 
        code is not None), key=lambda item: abs(item[1] - class_))[0]