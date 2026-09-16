def coords(self):
    if self.type not in {EventType.TOUCH_DOWN, EventType.TOUCH_MOTION}:
        raise AttributeError(_wrong_prop.format(self.type))
    x = self._libinput.libinput_event_touch_get_x(self._handle)
    y = self._libinput.libinput_event_touch_get_y(self._handle)
    return x, y