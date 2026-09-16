def refresh(self):
    self.get_devices(refresh=True)
    self.get_automations(refresh=True)