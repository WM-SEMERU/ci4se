def emails(self, drop_collections=True):
    base_df = self._data
    if drop_collections is True:
        out_df = self._drop_collections(base_df)
    else:
        out_df = base_df
    return out_df