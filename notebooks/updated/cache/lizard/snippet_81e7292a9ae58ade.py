def _pop(self, command, *args, **kwargs):
    result = self._traverse_command(command, *args, **kwargs)
    if self.indexable:
        self.deindex([result])
    return result