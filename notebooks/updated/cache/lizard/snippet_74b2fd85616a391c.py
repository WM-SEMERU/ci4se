def focus_prev_unfolded(self):
    self.focus_property(lambda x: not x.is_collapsed(x.root), self._tree.
        prev_position)