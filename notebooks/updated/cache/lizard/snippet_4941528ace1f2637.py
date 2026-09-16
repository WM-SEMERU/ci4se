def overlap(self, value):
    if value == 0:
        self._element._remove_overlap()
        return
    self._element.get_or_add_overlap().val = value