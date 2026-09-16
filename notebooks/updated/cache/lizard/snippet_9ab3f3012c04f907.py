def delete(self, key):
    if not is_string(key):
        raise Exception('Key must be string')
    if len(key) > 32:
        raise Exception('Max key length is 32')
    self.root_node = self._delete_and_delete_storage(self.root_node,
        bin_to_nibbles(to_string(key)))
    self._update_root_hash()