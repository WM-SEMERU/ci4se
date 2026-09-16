def make_dict_from_vector(in_array):
    out_dict = {}
    for i, k in enumerate(in_array):
        if k < 0:
            continue
        try:
            out_dict[k].append(i)
        except KeyError:
            out_dict[k] = [i]
    return out_dict