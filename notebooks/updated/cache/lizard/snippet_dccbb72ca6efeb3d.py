def go_up(self):
    if self.current_option > 0:
        self.current_option += -1
    else:
        self.current_option = len(self.items) - 1
    self.draw()