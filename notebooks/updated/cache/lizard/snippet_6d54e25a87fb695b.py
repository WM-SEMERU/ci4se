def _change_to_noFill_bg(self):
    self._remove_bg()
    bg = self.get_or_add_bg()
    bg.add_noFill_bgPr()
    return bg