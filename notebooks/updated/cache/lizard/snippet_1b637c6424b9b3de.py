def reprfunc(val, precision=None):
    r
    if isinstance(val, six.string_types):
        repr_ = repr(val)
        if repr_.startswith("u'") or repr_.startswith('u"'):
            repr_ = repr_[1:]
    elif precision is not None and (isinstance(val, float) or util_type.
        is_float(val)):
        return scalar_str(val, precision)
    elif isinstance(val, type):
        import utool as ut
        repr_ = ut.type_str(val)
    else:
        repr_ = repr(val)
    return repr_