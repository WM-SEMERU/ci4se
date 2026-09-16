def accel_increase_height(self, *args):
    height = self.settings.general.get_int('window-height')
    self.settings.general.set_int('window-height', min(height + 2, 100))
    return True