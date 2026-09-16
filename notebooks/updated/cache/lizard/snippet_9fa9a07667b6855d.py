def write_title(self, title: str, title_color: str=YELLOW,
    hyphen_line_color: str=WHITE):
    self.write_line(title_color + title)
    self.write_line(hyphen_line_color + '=' * (len(title) + 3))