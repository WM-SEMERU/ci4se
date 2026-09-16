def has_scope(context=None):
    if not booted(context):
        return False
    _sd_version = version(context)
    if _sd_version is None:
        return False
    return _sd_version >= 205