def attached_window(self):
    active_windows = []
    for window in self._windows:
        if 'window_active' in window:
            if window.get('window_active') == '1':
                active_windows.append(Window(session=self, **window))
            else:
                continue
    if len(active_windows) == int(1):
        return active_windows[0]
    else:
        raise exc.LibTmuxException('multiple active windows found. %s' %
            active_windows)
    if len(self._windows) == int(0):
        raise exc.LibTmuxException('No Windows')