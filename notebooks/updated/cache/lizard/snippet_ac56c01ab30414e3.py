def remove_from_postmortem_exclusion_list(cls, pathname, bits=None):
    if bits is None:
        bits = cls.bits
    elif bits not in (32, 64):
        raise NotImplementedError('Unknown architecture (%r bits)' % bits)
    if bits == 32 and cls.bits == 64:
        keyname = (
            'HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\AeDebug\\AutoExclusionList'
            )
    else:
        keyname = (
            'HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\AeDebug\\AutoExclusionList'
            )
    try:
        key = cls.registry[keyname]
    except KeyError:
        return
    try:
        del key[pathname]
    except KeyError:
        return