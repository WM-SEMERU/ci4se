def _expand_fcp_list(fcp_list):
    LOG.debug('Expand FCP list %s' % fcp_list)
    if not fcp_list:
        return set()
    range_pattern = '[0-9a-fA-F]{1,4}(-[0-9a-fA-F]{1,4})?'
    match_pattern = '^(%(range)s)(;%(range)s)*$' % {'range': range_pattern}
    if not re.match(match_pattern, fcp_list):
        errmsg = 'Invalid FCP address %s' % fcp_list
        raise exception.SDKInternalError(msg=errmsg)
    fcp_devices = set()
    for _range in fcp_list.split(';'):
        if '-' not in _range:
            fcp_addr = int(_range, 16)
            fcp_devices.add('%04x' % fcp_addr)
        else:
            _min, _max = _range.split('-')
            _min = int(_min, 16)
            _max = int(_max, 16)
            for fcp_addr in range(_min, _max + 1):
                fcp_devices.add('%04x' % fcp_addr)
    return fcp_devices