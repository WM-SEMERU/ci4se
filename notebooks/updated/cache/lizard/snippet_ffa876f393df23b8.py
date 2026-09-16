def update_cached_fields(*args):
    for a in args:
        if a is not None:
            if hasattr(a, '__iter__'):
                for e in a:
                    e.update_cached_fields()
            else:
                a.update_cached_fields()