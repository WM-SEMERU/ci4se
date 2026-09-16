def s_find_first(pred, first, lst):
    if pred(first):
        return first
    elif lst:
        return s_find_first(pred, unquote(lst[0]), lst[1:])
    else:
        return None