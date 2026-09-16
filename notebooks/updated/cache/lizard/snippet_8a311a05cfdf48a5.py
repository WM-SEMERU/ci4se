def slider_position(self):
    position = self._libinput.libinput_event_tablet_tool_get_slider_position(
        self._handle)
    changed = self._libinput.libinput_event_tablet_tool_slider_has_changed(self
        ._handle)
    return position, changed