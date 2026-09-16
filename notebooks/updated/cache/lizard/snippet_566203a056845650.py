def set_style(self, style):
    if style is not None:
        try:
            self.style.update(style)
        except ValueError:
            for s in style.split(';'):
                k, v = s.split(':', 1)
                self.style[k.strip()] = v.strip()