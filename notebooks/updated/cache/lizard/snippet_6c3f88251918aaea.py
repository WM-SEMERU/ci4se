def add(self, parent, child):
    if parent not in self:
        if parent.stype != 'boolean':
            raise ValueError('Parent sensor %r is not boolean' % child)
        self._parent_to_not_ok[parent] = set()
    if child not in self:
        if child.stype != 'boolean':
            raise ValueError('Child sensor %r is not booelan' % child)
        self._parent_to_not_ok[child] = set()
    self.add_links(parent, (child,))