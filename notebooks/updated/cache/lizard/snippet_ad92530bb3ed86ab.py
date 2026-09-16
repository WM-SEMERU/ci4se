def show_selection(self, star):
    try:
        self._select_flag = True
        self.mark_selection(star)
    finally:
        self._select_flag = False