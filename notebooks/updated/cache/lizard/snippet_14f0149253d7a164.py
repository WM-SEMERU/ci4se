def history(self, bar_count, frequency, field, ffill=True):
    return self.get_history_window(bar_count, frequency, self.
        _calculate_universe(), field, ffill)