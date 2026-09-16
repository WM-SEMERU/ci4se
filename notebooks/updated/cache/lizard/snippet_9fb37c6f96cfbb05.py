def button(self):
    if self.type != EventType.TABLET_TOOL_BUTTON:
        raise AttributeError(_wrong_prop.format(self.type))
    return self._libinput.libinput_event_tablet_tool_get_button(self._handle)