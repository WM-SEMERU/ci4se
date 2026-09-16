def delta(self):
    if self.type not in {EventType.GESTURE_SWIPE_UPDATE, EventType.
        GESTURE_PINCH_UPDATE}:
        raise AttributeError(_wrong_prop.format(self.type))
    delta_x = self._libinput.libinput_event_gesture_get_dx(self._handle)
    delta_y = self._libinput.libinput_event_gesture_get_dy(self._handle)
    return delta_x, delta_y