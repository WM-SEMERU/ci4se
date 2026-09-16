def _confirm_pos(self, pos):
    candidate = None
    if self._get_node(self._treelist, pos) is not None:
        candidate = pos
    return candidate