def listclip(list_, num, fromback=False):
    r
    if num is None:
        num_ = len(list_)
    else:
        num_ = min(len(list_), num)
    if fromback:
        sublist = list_[-num_:]
    else:
        sublist = list_[:num_]
    return sublist