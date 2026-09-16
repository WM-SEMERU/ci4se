def cycle_focus(self):
    windows = self.windows()
    new_index = (windows.index(self.active_window) + 1) % len(windows)
    self.active_window = windows[new_index]