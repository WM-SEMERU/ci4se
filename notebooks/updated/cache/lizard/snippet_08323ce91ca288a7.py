def _get_minute_window_data(self, assets, field, minutes_for_window):
    return self._minute_history_loader.history(assets, minutes_for_window,
        field, False)