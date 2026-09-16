def list_components(self):
    overlays = list(self._component_overlays)
    items = self.kvstore.get_all()
    return overlays + [x[0] for x in items if not x[0].startswith('config:')]