def _del(self, command, *args, **kwargs):
    if self.indexable:
        self.deindex()
    return self._traverse_command(command, *args, **kwargs)