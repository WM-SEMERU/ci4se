def examine(self):
    if self._changes:
        return self._changes.pop()
    action_file = None
    if self._changed:
        self._changed = False
        action_file = self._action_file or True
    return action_file, None