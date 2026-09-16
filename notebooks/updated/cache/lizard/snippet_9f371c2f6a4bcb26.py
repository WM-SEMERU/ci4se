def expand_focussed(self):
    if implementsCollapseAPI(self._tree):
        w, focuspos = self.get_focus()
        self._tree.expand(focuspos)
        self._walker.clear_cache()
        self.refresh()