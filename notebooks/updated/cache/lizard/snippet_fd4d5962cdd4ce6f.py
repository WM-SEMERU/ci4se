def collapse_all(self):
    if implementsCollapseAPI(self._tree):
        self._tree.collapse_all()
        self.set_focus(self._tree.root)
        self._walker.clear_cache()
        self.refresh()