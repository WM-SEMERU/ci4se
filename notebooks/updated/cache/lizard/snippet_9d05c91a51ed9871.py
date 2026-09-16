def prefix(*kinds):

    def wrap(fn):
        try:
            fn.prefix_kinds.extend(kinds)
        except AttributeError:
            fn.prefix_kinds = list(kinds)
        return fn
    return wrap