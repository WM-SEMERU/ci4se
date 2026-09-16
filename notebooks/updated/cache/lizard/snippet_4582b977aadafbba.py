def get_homogenous_list_type(list_):
    if HAVE_NUMPY and isinstance(list_, np.ndarray):
        item = list_
    elif isinstance(list_, list) and len(list_) > 0:
        item = list_[0]
    else:
        item = None
    if item is not None:
        if is_float(item):
            type_ = float
        elif is_int(item):
            type_ = int
        elif is_bool(item):
            type_ = bool
        elif is_str(item):
            type_ = str
        else:
            type_ = get_type(item)
    else:
        type_ = None
    return type_