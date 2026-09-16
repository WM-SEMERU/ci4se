def extendlist(lst, i, value=''):
    if i < len(lst):
        pass
    else:
        lst.extend([value] * (i - len(lst) + 1))