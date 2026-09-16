def enable_disable(self):
    if self.enabled:
        self.data['enabled'] = False
    else:
        self.data['enabled'] = True
    self.update()