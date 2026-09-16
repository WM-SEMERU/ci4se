def validate_cmaps(cmaps):
    cmaps = {validate_str(key): validate_colorlist(val) for key, val in cmaps}
    for key, val in six.iteritems(cmaps):
        cmaps.setdefault(key + '_r', val[::-1])
    return cmaps