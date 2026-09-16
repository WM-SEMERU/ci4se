def debugger():
    sdb = _current[0]
    if sdb is None or not sdb.active:
        sdb = _current[0] = Sdb()
    return sdb