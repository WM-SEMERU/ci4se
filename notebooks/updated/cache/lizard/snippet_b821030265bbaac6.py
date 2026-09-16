def _viewbox_set(self, viewbox):
    self._viewbox = viewbox
    viewbox.events.mouse_press.connect(self.viewbox_mouse_event)
    viewbox.events.mouse_release.connect(self.viewbox_mouse_event)
    viewbox.events.mouse_move.connect(self.viewbox_mouse_event)
    viewbox.events.mouse_wheel.connect(self.viewbox_mouse_event)
    viewbox.events.resize.connect(self.viewbox_resize_event)