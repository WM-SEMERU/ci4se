def tally(self, name, value):
    value = value or 0
    if 'used' not in self.usages[name]:
        self.usages[name]['used'] = 0
    self.usages[name]['used'] += int(value)
    self.update_available(name)