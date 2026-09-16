def ring_number(self):
    if self.type != EventType.TABLET_PAD_RING:
        raise AttributeError(_wrong_prop.format(self.type))
    return self._libinput.libinput_event_tablet_pad_get_ring_number(self.
        _handle)