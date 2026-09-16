def _spot_col(self, colname):
    try:
        col = self._spot_cols[colname]
    except KeyError:
        col = self._spot_cols[colname] = self._table[colname]
    return col