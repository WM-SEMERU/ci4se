def set_colors(self, fg=None, bg=None):
    if fg is not None:
        self._fg = _format_color(fg, self._fg)
    if bg is not None:
        self._bg = _format_color(bg, self._bg)