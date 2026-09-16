def _get_color(self):
    if self.clicked and self.hovered:
        color = mix(self.color, BLACK, 0.8)
    elif self.hovered and not self.flags & self.NO_HOVER:
        color = mix(self.color, BLACK, 0.93)
    else:
        color = self.color
    self.text.bg_color = color
    return color