def prev(self):
    prev_index = self.index - 1
    prev_handle = self._browser.driver.window_handles[prev_index]
    return Window(self._browser, prev_handle)