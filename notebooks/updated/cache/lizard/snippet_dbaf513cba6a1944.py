def on_mouse_move(self, event):
    if event.modifiers:
        return
    if event.is_dragging:
        x0, y0 = self._normalize(event.press_event.pos)
        x1, y1 = self._normalize(event.last_event.pos)
        x, y = self._normalize(event.pos)
        dx, dy = x - x1, y - y1
        if event.button == 1:
            self.pan_delta((dx, dy))
        elif event.button == 2:
            c = np.sqrt(self.size[0]) * 0.03
            self.zoom_delta((dx, dy), (x0, y0), c=c)