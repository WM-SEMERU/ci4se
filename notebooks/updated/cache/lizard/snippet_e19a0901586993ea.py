def match_metric(regex):
    if _TRAFFICCTL:
        cmd = _traffic_ctl('metric', 'match', regex)
    else:
        cmd = _traffic_ctl('-m', regex)
    return _subprocess(cmd)