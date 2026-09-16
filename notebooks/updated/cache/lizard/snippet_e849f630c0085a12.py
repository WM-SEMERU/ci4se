def default_sort_key(item, order=None):
    from sympy.core import S, Basic
    from sympy.core.sympify import sympify, SympifyError
    from sympy.core.compatibility import iterable
    if isinstance(item, Basic):
        return item.sort_key(order=order)
    if iterable(item, exclude=string_types):
        if isinstance(item, dict):
            args = item.items()
            unordered = True
        elif isinstance(item, set):
            args = item
            unordered = True
        else:
            args = list(item)
            unordered = False
        args = [default_sort_key(arg, order=order) for arg in args]
        if unordered:
            args = sorted(args)
        cls_index, args = 10, (len(args), tuple(args))
    else:
        if not isinstance(item, string_types):
            try:
                item = sympify(item)
            except SympifyError:
                pass
            else:
                if isinstance(item, Basic):
                    return default_sort_key(item)
        cls_index, args = 0, (1, (str(item),))
    return (cls_index, 0, item.__class__.__name__), args, S.One.sort_key(
        ), S.One