def _set_focused_item(self, item):
    if not item:
        return self._del_focused_item()
    if item.model is not self._selection.focus:
        self.queue_draw_item(self._focused_item, item)
        self._selection.focus = item.model
        self.emit('focus-changed', item)