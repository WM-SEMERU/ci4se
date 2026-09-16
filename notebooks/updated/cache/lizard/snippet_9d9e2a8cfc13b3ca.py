def axis_source(self):
    if self.type != EventType.POINTER_AXIS:
        raise AttributeError(_wrong_prop.format(self.type))
    return self._libinput.libinput_event_pointer_get_axis_source(self._handle)