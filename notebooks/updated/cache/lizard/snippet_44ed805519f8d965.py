def multi_click(self, locator, params=None, timeout=None):
    platform = self.execute_script('return navigator.platform')
    multi_key = Keys.COMMAND if 'mac' in platform.lower(
        ) else Keys.LEFT_CONTROL
    self._click(locator, params, timeout, multi_key)