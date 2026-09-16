def prepare(self, ansi='', ensure_trailing_newline=False):
    body, styles = self.apply_regex(ansi)
    if ensure_trailing_newline and _needs_extra_newline(body):
        body += '\n'
    self._attrs = {'dark_bg': self.dark_bg, 'line_wrap': self.line_wrap,
        'font_size': self.font_size, 'body': body, 'styles': styles}
    return self._attrs