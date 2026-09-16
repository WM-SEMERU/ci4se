def undo(self):
    args = self._undo_stack.back()
    if args is None:
        return
    self._data = deepcopy(self._data_base)
    for clusters, field, value, up, undo_state in self._undo_stack:
        if clusters is not None:
            self.set(field, clusters, value, add_to_stack=False)
    up, undo_state = args[-2:]
    up.history = 'undo'
    up.undo_state = undo_state
    self.emit('cluster', up)
    return up