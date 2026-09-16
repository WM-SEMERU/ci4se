def _update_staticmethod(self, oldsm, newsm):
    self._update(None, None, oldsm.__get__(0), newsm.__get__(0))