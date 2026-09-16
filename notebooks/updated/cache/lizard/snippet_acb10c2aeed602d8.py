def _load_prev(self):
    if self._load_by_date:
        prev_date = self.date - pds.DateOffset(days=1)
        return self._load_data(date=prev_date)
    else:
        return self._load_data(fid=self._fid - 1)