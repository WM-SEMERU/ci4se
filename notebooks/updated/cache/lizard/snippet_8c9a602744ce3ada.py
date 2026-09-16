def flatten(self):
    [c.allocate(-c.value) for c in self._childrenv if c.value != 0]