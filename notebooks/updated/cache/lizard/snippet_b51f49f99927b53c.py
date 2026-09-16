def _extract(self, source, *args, **kwargs):
    self._data = mbox_to_pandas(source)
    self._data['MessageID'] = pd.Series(range(0, len(self._data)))