def _GetStat(self):
    stat_object = super(VShadowFileEntry, self)._GetStat()
    if self._vshadow_store is not None:
        stat_object.size = self._vshadow_store.volume_size
    return stat_object