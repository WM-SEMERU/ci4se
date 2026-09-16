def match_version(desired, available, cmp_func=None, ignore_epoch=False):
    oper, version = split_comparison(desired)
    if not oper:
        oper = '=='
    for candidate in available:
        if salt.utils.versions.compare(ver1=candidate, oper=oper, ver2=
            version, cmp_func=cmp_func, ignore_epoch=ignore_epoch):
            return candidate
    return None