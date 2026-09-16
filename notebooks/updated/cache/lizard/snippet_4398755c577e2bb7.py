def _remove_otiose(lst):
    listtype = type([])
    while type(lst) == listtype and len(lst) == 1:
        lst = lst[0]
    return lst