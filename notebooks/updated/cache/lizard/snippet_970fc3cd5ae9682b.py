def _add(self, command, *args, **kwargs):
    if self.indexable:
        self.index(args)
    return self._traverse_command(command, *args, **kwargs)