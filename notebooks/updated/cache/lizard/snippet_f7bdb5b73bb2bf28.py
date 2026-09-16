def wheel_delta(self):
    delta = self._libinput.libinput_event_tablet_tool_get_wheel_delta(self.
        _handle)
    changed = self._libinput.libinput_event_tablet_tool_wheel_has_changed(self
        ._handle)
    return delta, changed