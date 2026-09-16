def add_header_callback(self, cb, port, channel, port_mask=255,
    channel_mask=255):
    self.cb.append(_CallbackContainer(port, port_mask, channel,
        channel_mask, cb))