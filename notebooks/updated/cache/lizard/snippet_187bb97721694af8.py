def lock(self):
    self.password = None
    self.keyfile = None
    self.groups[:] = []
    self.entries[:] = []
    self._group_order[:] = []
    self._entry_order[:] = []
    self.root_group = v1Group()
    self._num_groups = 1
    self._num_entries = 0
    return True