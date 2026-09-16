def has_operator(context, x, y):
    user = x.eval(context)
    perm = y.eval(context)
    if isinstance(perm, (list, tuple)):
        perm, obj = perm
    else:
        obj = None
    return user.has_perm(perm, obj)