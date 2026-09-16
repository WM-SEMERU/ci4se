def set_config(variable, value):
    if _TRAFFICCTL:
        cmd = _traffic_ctl('config', 'set', variable, value)
    else:
        cmd = _traffic_line('-s', variable, '-v', value)
    log.debug('Setting %s to %s', variable, value)
    return _subprocess(cmd)