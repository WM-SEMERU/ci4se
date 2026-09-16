def onselection(self, widget):
    self._selected_key = None
    for k in self.children:
        if self.children[k] == widget:
            self._selected_key = k
            if self._selected_item is not None and self._selectable:
                self._selected_item.attributes['selected'] = False
            self._selected_item = self.children[self._selected_key]
            if self._selectable:
                self._selected_item.attributes['selected'] = True
            break
    return self._selected_key,