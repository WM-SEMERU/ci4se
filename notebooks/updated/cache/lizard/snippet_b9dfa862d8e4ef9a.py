def long_press_keycode(self, keycode, metastate=None):
    driver = self._current_application()
    driver.long_press_keycode(int(keycode), metastate)