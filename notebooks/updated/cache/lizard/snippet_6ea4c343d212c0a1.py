def hdate(self):
    if self._last_updated == 'hdate':
        return self._hdate
    return conv.jdn_to_hdate(self._jdn)