def delta_unaccelerated(self):
    if self.type != EventType.POINTER_MOTION:
        raise AttributeError(_wrong_prop.format(self.type))
    delta_x = self._libinput.libinput_event_pointer_get_dx_unaccelerated(self
        ._handle)
    delta_y = self._libinput.libinput_event_pointer_get_dy_unaccelerated(self
        ._handle)
    return delta_x, delta_y