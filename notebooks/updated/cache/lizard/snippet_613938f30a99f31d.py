def _validate(self, writing=False):
    if not (len(self.index) == len(self.channel_type) and len(self.
        channel_type) == len(self.association)):
        msg = (
            'The length of the index ({index}), channel_type ({channel_type}), and association ({association}) inputs must be the same.'
            )
        msg = msg.format(index=len(self.index), channel_type=len(self.
            channel_type), association=len(self.association))
        self._dispatch_validation_error(msg, writing=writing)
    if any(x not in [0, 1, 2, 65535] for x in self.channel_type):
        msg = """channel_type specified as {channel_type}, but all values must be in the set of

    0     - colour image data for associated color
    1     - opacity
    2     - premultiplied opacity
    65535 - unspecified
"""
        msg = msg.format(channel_type=self.channel_type)
        self._dispatch_validation_error(msg, writing=writing)