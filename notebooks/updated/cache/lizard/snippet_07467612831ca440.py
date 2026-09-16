def cancelled(self):
    if self.type not in {EventType.GESTURE_SWIPE_END, EventType.
        GESTURE_PINCH_END}:
        raise AttributeError(_wrong_prop.format(self.type))
    return self._libinput.libinput_event_gesture_get_cancelled(self._handle)