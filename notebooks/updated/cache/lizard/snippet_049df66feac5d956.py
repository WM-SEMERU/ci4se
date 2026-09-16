def solar_midnight_utc(self, date, longitude):
    julianday = self._julianday(date)
    newt = self._jday_to_jcentury(julianday + 0.5 + -longitude / 360.0)
    eqtime = self._eq_of_time(newt)
    timeUTC = -longitude * 4.0 - eqtime
    timeUTC = timeUTC / 60.0
    hour = int(timeUTC)
    minute = int((timeUTC - hour) * 60)
    second = int(((timeUTC - hour) * 60 - minute) * 60)
    if second > 59:
        second -= 60
        minute += 1
    elif second < 0:
        second += 60
        minute -= 1
    if minute > 59:
        minute -= 60
        hour += 1
    elif minute < 0:
        minute += 60
        hour -= 1
    if hour < 0:
        hour += 24
        date -= datetime.timedelta(days=1)
    midnight = datetime.datetime(date.year, date.month, date.day, hour,
        minute, second)
    midnight = pytz.UTC.localize(midnight)
    return midnight