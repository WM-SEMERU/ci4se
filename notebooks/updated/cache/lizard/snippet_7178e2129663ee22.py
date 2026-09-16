def unique_list_dicts(dlist, key):
    return list(dict((val[key], val) for val in dlist).values())