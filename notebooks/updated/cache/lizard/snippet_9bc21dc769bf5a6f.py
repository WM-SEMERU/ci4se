def _filtered_list(self, selector):
    res = []
    for elem in self.obj:
        self._append(elem, selector, res)
    return res