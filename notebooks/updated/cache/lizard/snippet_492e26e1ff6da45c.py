def distance(self):
    distance = self._libinput.libinput_event_tablet_tool_get_distance(self.
        _handle)
    changed = self._libinput.libinput_event_tablet_tool_distance_has_changed(
        self._handle)
    return distance, changed