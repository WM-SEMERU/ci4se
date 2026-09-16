def monthly_wind_dirs(self):
    mwd = zip(*self._monthly_wind_dirs)
    return [self._wind_dirs[mon.index(max(mon))] for mon in mwd]