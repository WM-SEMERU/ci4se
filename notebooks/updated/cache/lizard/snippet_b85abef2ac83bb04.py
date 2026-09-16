def _fetch_items(self):
    if self._items is None:
        self._items = list(self.engine.items(self))
    return self._items