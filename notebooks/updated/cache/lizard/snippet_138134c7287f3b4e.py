def cat(expr, others=None, sep=None, na_rep=None):
    if others is not None:
        from .strings import _cat as cat_str
        return cat_str(expr, others, sep=sep, na_rep=na_rep)
    return _cat(expr, sep=sep, na_rep=na_rep)