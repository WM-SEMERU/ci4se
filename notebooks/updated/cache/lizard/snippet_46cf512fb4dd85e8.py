def on_touch_move(self, touch):
    if touch.grab_current is not self:
        return False
    self.center = touch.pos
    return True