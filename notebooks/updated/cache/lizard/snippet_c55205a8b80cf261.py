def any_has_focus(self):
    f = self.hasFocus() or self.parent.hasFocus() or self.tips.hasFocus(
        ) or self.canvas.hasFocus()
    return f