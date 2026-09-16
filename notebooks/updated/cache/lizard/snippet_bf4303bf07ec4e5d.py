def is_after(self, ts):
    if self.timestamp >= int(calendar.timegm(ts.timetuple())):
        return True
    return False