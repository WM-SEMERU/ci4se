def toggle(self, section, option):
    self.set(section, option, not self.get(section, option))