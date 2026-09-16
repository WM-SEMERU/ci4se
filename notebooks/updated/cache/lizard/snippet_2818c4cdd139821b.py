def heat_setting(self, value):
    if value not in range(0, 4):
        raise exceptions.RoasterValueError
    self._heat_setting.value = value