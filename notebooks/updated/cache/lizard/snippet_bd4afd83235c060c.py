def _get_dict_value_by_path(d, path):
    tmp_path = deepcopy(path)
    try:
        while len(tmp_path) > 0:
            k = tmp_path.pop(0)
            d = d[k]
        return d
    except:
        return None