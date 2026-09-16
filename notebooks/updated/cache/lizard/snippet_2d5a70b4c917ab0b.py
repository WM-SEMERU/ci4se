def convert_dicts(d, to_class=AttrDictWrapper, from_class=dict):
    d_ = to_class()
    for key, value in d.iteritems():
        if isinstance(value, from_class):
            d_[key] = convert_dicts(value, to_class=to_class, from_class=
                from_class)
        else:
            d_[key] = value
    return d_