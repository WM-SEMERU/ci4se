def str2dict_values(str_in):
    tmp_dict = str2dict(str_in)
    if tmp_dict is None:
        return None
    return [tmp_dict[key] for key in sorted(k for k in tmp_dict)]