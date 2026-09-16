def doys_int(self):
    if not self._is_reversed:
        return self._calc_daystamps(self.st_time, self.end_time)
    else:
        doys_st = self._calc_daystamps(self.st_time, DateTime.from_hoy(8759))
        doys_end = self._calc_daystamps(DateTime.from_hoy(0), self.end_time)
        return doys_st + doys_end