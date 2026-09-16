def filter_items(self, items):
    items = self._filter_active(items)
    items = self._filter_in_nav(items)
    return items