def get_all(limit=''):
    limit = limit.lower()
    if limit == 'upstart':
        return sorted(_upstart_services())
    elif limit == 'sysvinit':
        return sorted(_sysv_services())
    else:
        return sorted(_sysv_services() + _upstart_services())