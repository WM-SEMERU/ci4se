def tab(self):
    for stop in sorted(self.tabstops):
        if self.cursor.x < stop:
            column = stop
            break
    else:
        column = self.columns - 1
    self.cursor.x = column