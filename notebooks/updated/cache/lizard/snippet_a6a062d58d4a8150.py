def _uncheck_ancestor(self, item):
    self.change_state(item, 'unchecked')
    parent = self.parent(item)
    if parent:
        children = self.get_children(parent)
        b = [('unchecked' in self.item(c, 'tags')) for c in children]
        if False in b:
            self._tristate_parent(parent)
        else:
            self._uncheck_ancestor(parent)