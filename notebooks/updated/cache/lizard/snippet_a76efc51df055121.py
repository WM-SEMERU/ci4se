def load_blind(self, item):
    blind = Blind.from_config(self.pyvlx, item)
    self.add(blind)