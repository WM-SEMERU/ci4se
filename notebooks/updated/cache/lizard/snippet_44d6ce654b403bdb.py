def focus_next(self):
    w, focuspos = self.get_focus()
    next = self._tree.next_position(focuspos)
    if next is not None:
        self.set_focus(next)