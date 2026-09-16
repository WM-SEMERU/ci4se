def _additional_rows_date2int(self, keys, rows):
    for row in rows:
        for key_start_date, key_end_date in keys:
            if key_start_date not in [self._key_start_date, self._key_end_date
                ]:
                row[key_start_date] = self._date2int(row[key_start_date])
            if key_end_date not in [self._key_start_date, self._key_end_date]:
                row[key_end_date] = self._date2int(row[key_end_date])