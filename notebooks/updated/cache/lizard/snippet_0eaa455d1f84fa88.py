def clear_alarms(alarm):
    if _TRAFFICCTL:
        cmd = _traffic_ctl('alarm', 'clear', alarm)
    else:
        cmd = _traffic_line('--clear_alarms', alarm)
    return _subprocess(cmd)