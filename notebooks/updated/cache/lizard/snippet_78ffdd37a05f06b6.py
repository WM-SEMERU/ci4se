def on_event(self, event):
    state = self.state
    if isinstance(event, wx.MouseEvent):
        self.on_mouse_event(event)
    if isinstance(event, wx.KeyEvent):
        self.on_key_event(event)
    if isinstance(event, wx.MouseEvent) and not event.ButtonIsDown(wx.
        MOUSE_BTN_ANY) and event.GetWheelRotation() == 0:
        return
    evt = mp_util.object_container(event)
    pt = self.image_coordinates(wx.Point(evt.X, evt.Y))
    evt.X = pt.x
    evt.Y = pt.y
    state.out_queue.put(evt)