def set_arc(self, arc):
    _send_vendor_setup(self.handle, SET_RADIO_ARC, arc, 0, ())
    self.arc = arc