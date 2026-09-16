def setattr(d, **kwarg):
    if _meta not in d:
        d[_meta] = dict()
    for k, v in kwarg.items():
        d[_meta][k] = v