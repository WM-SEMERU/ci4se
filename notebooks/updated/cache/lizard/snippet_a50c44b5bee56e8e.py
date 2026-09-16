def _update_all_devices(self):
    self.all_devices = []
    self.all_devices.extend(self.keyboards)
    self.all_devices.extend(self.mice)
    self.all_devices.extend(self.gamepads)
    self.all_devices.extend(self.other_devices)