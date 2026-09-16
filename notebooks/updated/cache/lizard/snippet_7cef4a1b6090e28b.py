def update(self, key, value):
    if not is_string(key):
        raise Exception('Key must be string')
    if not is_string(value):
        raise Exception('Value must be string')
    old_root = copy.deepcopy(self.root_node)
    self.root_node = self._update_and_delete_storage(self.root_node,
        bin_to_nibbles(to_string(key)), to_string(value))
    self.replace_root_hash(old_root, self.root_node)