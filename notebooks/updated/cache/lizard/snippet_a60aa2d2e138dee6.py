def transform_coords(self, width, height):
    x = self._libinput.libinput_event_tablet_tool_get_x_transformed(self.
        _handle, width)
    y = self._libinput.libinput_event_tablet_tool_get_y_transformed(self.
        _handle, height)
    x_changed = self._libinput.libinput_event_tablet_tool_x_has_changed(self
        ._handle)
    y_changed = self._libinput.libinput_event_tablet_tool_y_has_changed(self
        ._handle)
    return (x, y), x_changed or y_changed