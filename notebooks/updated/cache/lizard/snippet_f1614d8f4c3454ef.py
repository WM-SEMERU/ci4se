def register_minter(self, name, minter):
    assert name not in self.minters
    self.minters[name] = minter