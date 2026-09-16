def _getFromTime(self, atDate=None):
    return getLocalTime(self.except_date, self.time_from, self.tz)