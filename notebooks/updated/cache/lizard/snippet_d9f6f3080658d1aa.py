def set_trace(frame=None, skip=0, server=None, port=None):
    frame = frame or sys._getframe().f_back
    for i in range(skip):
        if not frame.f_back:
            break
        frame = frame.f_back
    wdb = Wdb.get(server=server, port=port)
    wdb.set_trace(frame)
    return wdb