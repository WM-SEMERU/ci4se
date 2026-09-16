def get_rows(self, sort=False):
    ret = []
    for _, rows in (sorted(self._rows.items()) if sort else self._rows.items()
        ):
        self._rows_int2date(rows)
        ret.extend(rows)
    return ret