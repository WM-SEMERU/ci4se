def mode_key_up(self, viewer, keyname):
    if keyname not in self.mode_map:
        return False
    bnch = self.mode_map[keyname]
    if self._kbdmode == bnch.name:
        if bnch.type == 'held':
            if self._button == 0:
                self.reset_mode(viewer)
            else:
                self._delayed_reset = True
        return True
    return False