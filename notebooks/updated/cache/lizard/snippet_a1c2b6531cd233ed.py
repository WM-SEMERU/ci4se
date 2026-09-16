def add_many_to_dict_val_set(dict_obj, key, val_list):
    try:
        dict_obj[key].update(val_list)
    except KeyError:
        dict_obj[key] = set(val_list)