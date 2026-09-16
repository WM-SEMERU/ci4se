def hms2frame(hms, fps):
    import time
    t = time.strptime(hms, '%H:%M:%S')
    return (t.tm_hour * 60 * 60 + t.tm_min * 60 + t.tm_sec) * fps