def expand_limits(**kwargs):

    def as_list(key):
        with suppress(KeyError):
            if isinstance(kwargs[key], (int, float, str)):
                kwargs[key] = [kwargs[key]]
    if isinstance(kwargs, dict):
        as_list('x')
        as_list('y')
        data = pd.DataFrame(kwargs)
    else:
        data = kwargs
    mapping = {}
    for ae in (set(kwargs) & all_aesthetics):
        mapping[ae] = ae
    return geom_blank(mapping=mapping, data=data, inherit_aes=False)