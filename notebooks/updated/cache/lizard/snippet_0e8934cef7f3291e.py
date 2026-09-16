def erase_in_display(self, how=0, *args, **kwargs):
    super(HistoryScreen, self).erase_in_display(how, *args, **kwargs)
    if how == 3:
        self._reset_history()