def viewitems(obj, **kwargs):
    func = getattr(obj, 'viewitems', None)
    if not func:
        func = obj.items
    return func(**kwargs)