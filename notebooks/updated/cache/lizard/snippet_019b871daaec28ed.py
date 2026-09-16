def scale_dict_wet(C):
    return {k: (v / _scale_dict[k]) for k, v in C.items()}