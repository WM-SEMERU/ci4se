def pressure(self):
    pressure = self._libinput.libinput_event_tablet_tool_get_pressure(self.
        _handle)
    changed = self._libinput.libinput_event_tablet_tool_pressure_has_changed(
        self._handle)
    return pressure, changed