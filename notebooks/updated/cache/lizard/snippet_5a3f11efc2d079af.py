def delta(self):
    if self.type != EventType.POINTER_MOTION:
        raise AttributeError(_wrong_prop.format(self.type))
    delta_x = self._libinput.libinput_event_pointer_get_dx(self._handle)
    delta_y = self._libinput.libinput_event_pointer_get_dy(self._handle)
    return delta_x, delta_y