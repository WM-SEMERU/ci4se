def loop(self):
    self.active = True
    while self.selected_page and self.active:
        self.handle_selected_page()
    while self.active:
        self.draw()
        ch = self.term.stdscr.getch()
        self.controller.trigger(ch)
        while self.selected_page and self.active:
            self.handle_selected_page()
    return self.selected_page