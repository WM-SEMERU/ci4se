def upgrade_defaults(self):
    self.defaults.upgrade()
    self.reset_defaults(self.defaults.filename)