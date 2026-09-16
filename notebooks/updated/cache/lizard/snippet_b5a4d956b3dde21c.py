def _put_overlay(self, overlay_name, overlay):
    if not isinstance(overlay, dict):
        raise TypeError('Overlay must be dict')
    if set(self._identifiers()) != set(overlay.keys()):
        raise ValueError('Overlay keys must be dataset identifiers')
    self._storage_broker.put_overlay(overlay_name, overlay)