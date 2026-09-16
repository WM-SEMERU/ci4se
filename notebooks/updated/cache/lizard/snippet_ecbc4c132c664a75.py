def CalcDayOfWeek(self):
    year, month, day, day_of_week = self.value
    day_of_week = 255
    if year == 255:
        pass
    elif month in _special_mon_inv:
        pass
    elif day in _special_day_inv:
        pass
    else:
        try:
            today = time.mktime((year + 1900, month, day, 0, 0, 0, 0, 0, -1))
            day_of_week = time.gmtime(today)[6] + 1
        except OverflowError:
            pass
    self.value = year, month, day, day_of_week