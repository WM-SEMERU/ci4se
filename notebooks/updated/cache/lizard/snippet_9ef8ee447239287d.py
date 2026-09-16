def sid_day_index(self, sid, day):
    try:
        day_loc = self.sessions.get_loc(day)
    except Exception:
        raise NoDataOnDate('day={0} is outside of calendar={1}'.format(day,
            self.sessions))
    offset = day_loc - self._calendar_offsets[sid]
    if offset < 0:
        raise NoDataBeforeDate('No data on or before day={0} for sid={1}'.
            format(day, sid))
    ix = self._first_rows[sid] + offset
    if ix > self._last_rows[sid]:
        raise NoDataAfterDate('No data on or after day={0} for sid={1}'.
            format(day, sid))
    return ix