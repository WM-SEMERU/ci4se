def cut(list_, index=0):
    if isinstance(index, int):
        cut_ = lambda x: x[index]
    else:
        cut_ = lambda x: getattr(x, index)
    return list(map(cut_, list_))