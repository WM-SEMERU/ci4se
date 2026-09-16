def clean_single_dict(indict, prepend_to_keys=None, remove_keys_containing=None
    ):
    if not prepend_to_keys:
        prepend_to_keys = ''
    outdict = {}
    for k, v in indict.items():
        if remove_keys_containing:
            if remove_keys_containing in k:
                continue
        outdict[prepend_to_keys + k] = v[0]
    return outdict