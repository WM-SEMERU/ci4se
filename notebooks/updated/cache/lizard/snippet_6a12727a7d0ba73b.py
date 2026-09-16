def set_channel(self, channel):
    if channel != self.current_channel:
        _send_vendor_setup(self.handle, SET_RADIO_CHANNEL, channel, 0, ())
        self.current_channel = channel