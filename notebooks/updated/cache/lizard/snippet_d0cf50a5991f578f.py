def address_from_path(self, path=None):
    path = path if path else self._unique_hierarchical_string()
    return path, self.wallet.subkey_for_path(path).address()