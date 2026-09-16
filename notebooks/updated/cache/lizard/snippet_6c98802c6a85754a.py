def device_changed(self, old_state, new_state):
    if self._mounter.is_addable(new_state) and not self._mounter.is_addable(
        old_state) and not self._mounter.is_removable(old_state):
        self.auto_add(new_state)