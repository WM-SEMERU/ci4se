def make_tree(self):
    self.tree['is_ready'] = False
    leaf_count = len(self.tree['leaves'])
    if leaf_count > 0:
        self._unshift(self.tree['levels'], self.tree['leaves'])
        while len(self.tree['levels'][0]) > 1:
            self._unshift(self.tree['levels'], self._calculate_next_level())
    self.tree['is_ready'] = True