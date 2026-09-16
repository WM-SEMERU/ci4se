def on_touch_move(self, touch):
    if not self.dragging:
        touch.ungrab(self)
        return
    self.pos = touch.x - self.collide_x, touch.y - self.collide_y