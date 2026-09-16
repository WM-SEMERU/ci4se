def _getMyFirstDatetimeFrom(self):
    myStartDt = getAwareDatetime(self.repeat.dtstart, None, self.tz, dt.
        time.min)
    return self.__after(myStartDt, excludeCancellations=False)