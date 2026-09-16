def get_sid_string(principal):
    if principal is None:
        principal = 'NULL SID'
    try:
        return win32security.ConvertSidToStringSid(principal)
    except TypeError:
        principal = get_sid(principal)
    try:
        return win32security.ConvertSidToStringSid(principal)
    except pywintypes.error:
        log.exception('Invalid principal %s', principal)
        raise CommandExecutionError('Invalid principal {0}'.format(principal))