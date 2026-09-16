def spasser(inbox, s=None):
    seq = s or range(len(inbox))
    return [input_ for i, input_ in enumerate(inbox) if i in seq]