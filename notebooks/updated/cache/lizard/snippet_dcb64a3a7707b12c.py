def add_context_menu_items(self, items, replace_items=False):
    for label, action in items:
        assert isinstance(label, basestring)
        assert isinstance(action, basestring)
    if replace_items:
        self._context_menu_items = []
    self._context_menu_items.extend(items)
    self._listitem.addContextMenuItems(items, replace_items)