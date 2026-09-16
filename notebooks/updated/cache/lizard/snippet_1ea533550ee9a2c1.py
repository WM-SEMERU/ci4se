def seek_realtime(self, realtime):
    if isinstance(realtime, _datetime.datetime):
        realtime = int(float(realtime.strftime('%s.%f')) * 1000000)
    elif not isinstance(realtime, int):
        realtime = int(realtime * 1000000)
    return super(Reader, self).seek_realtime(realtime)