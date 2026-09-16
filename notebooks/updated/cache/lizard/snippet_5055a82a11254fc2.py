def _read_widget(self):
    getter = self._wid_info[self._wid][0]
    return getter(self._wid)