def asStructTime(self, tzinfo=None):
    dtime = self.asDatetime(tzinfo)
    if tzinfo is None:
        return dtime.utctimetuple()
    else:
        return dtime.timetuple()