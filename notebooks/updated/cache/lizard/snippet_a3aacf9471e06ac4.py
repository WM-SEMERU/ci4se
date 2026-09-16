def _wanna_emit_id_changed(self):
    if self._last_id != self._get_id():
        self._last_id = self._get_id()
        self.id_changed.emit()