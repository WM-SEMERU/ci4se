def _track_changes(self):
    if self._field and getattr(self._parent, '_track_changes', None
        ) is not None and self.untrack is False:
        self._parent._track_changes.add(self._field)