def show_progress(self):
    from pyemma import config
    if not hasattr(self, '_show_progress'):
        val = config.show_progress_bars
        self._show_progress = val
    elif not config.show_progress_bars:
        return False
    return self._show_progress