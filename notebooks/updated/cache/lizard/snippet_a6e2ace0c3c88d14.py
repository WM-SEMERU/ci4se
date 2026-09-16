def _massage_metakeys(dct, prfx):
    lowprefix = prfx.lower()
    ret = {}
    for k, v in list(dct.items()):
        if not k.lower().startswith(lowprefix):
            k = '%s%s' % (prfx, k)
        ret[k] = v
    return ret