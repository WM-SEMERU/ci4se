def needs_valid_channel(self, channel, maximum):
    assert isinstance(channel, int)
    assert isinstance(maximum, int)
    if channel < 1 and channel > maximum:
        self.parser_error('needs valid channel in channel byte')