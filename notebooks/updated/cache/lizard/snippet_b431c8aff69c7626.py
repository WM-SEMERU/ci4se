def close(self):
    target = self.prev if self.is_current and self.prev != self else None
    with switch_window(self._browser, self.name):
        self._browser.driver.close()
    if target is not None:
        target.is_current = True