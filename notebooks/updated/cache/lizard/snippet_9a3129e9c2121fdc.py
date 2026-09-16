def on_mouse_wheel(self, event):
    state = self.state
    if not state.can_zoom:
        return
    mousepos = self.image_coordinates(event.GetPosition())
    rotation = event.GetWheelRotation() / event.GetWheelDelta()
    oldzoom = self.zoom
    if rotation > 0:
        self.zoom /= 1.0 / (1.1 * rotation)
    elif rotation < 0:
        self.zoom /= 1.1 * -rotation
    if self.zoom > 10:
        self.zoom = 10
    elif self.zoom < 0.1:
        self.zoom = 0.1
    if oldzoom < 1 and self.zoom > 1:
        self.zoom = 1
    if oldzoom > 1 and self.zoom < 1:
        self.zoom = 1
    client_area = state.frame.GetClientSize()
    fit_window_zoom_level = min(float(client_area.x) / self.img.GetWidth(),
        float(client_area.y) / self.img.GetHeight())
    if self.zoom < fit_window_zoom_level:
        self.zoom = fit_window_zoom_level
    self.need_redraw = True
    new = self.image_coordinates(event.GetPosition())
    self.dragpos = wx.Point(self.dragpos.x - (new.x - mousepos.x), self.
        dragpos.y - (new.y - mousepos.y))
    self.limit_dragpos()