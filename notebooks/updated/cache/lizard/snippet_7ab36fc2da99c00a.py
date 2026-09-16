def bounce_local(drain=False):
    if _TRAFFICCTL:
        cmd = _traffic_ctl('server', 'restart')
    else:
        cmd = _traffic_line('-b')
    if drain:
        cmd = cmd + ['--drain']
    return _subprocess(cmd)