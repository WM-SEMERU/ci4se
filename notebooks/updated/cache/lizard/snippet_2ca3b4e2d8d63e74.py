def previous_theme(self):
    theme = self.term.theme_list.previous(self.term.theme)
    while not self.term.check_theme(theme):
        theme = self.term.theme_list.previous(theme)
    self.term.set_theme(theme)
    self.draw()
    message = self.term.theme.display_string
    self.term.show_notification(message, timeout=1)