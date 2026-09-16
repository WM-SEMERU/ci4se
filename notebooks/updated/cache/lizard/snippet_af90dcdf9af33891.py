def next_row(self):
    if self.mode == self.SYMBOL_MODE:
        self.select_row(+1)
        return
    next_row = self.current_row() + 1
    if next_row < self.count():
        if '</b></big><br>' in self.list.item(next_row).text():
            self.select_row(+2)
        else:
            self.select_row(+1)