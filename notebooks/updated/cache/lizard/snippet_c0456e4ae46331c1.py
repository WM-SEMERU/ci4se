def _create_channel(self, channel):
    super()._create_channel(channel)
    if 'EXCEPTS' in self._isupport:
        self.channels[channel]['exceptlist'] = None
    if 'INVEX' in self._isupport:
        self.channels[channel]['inviteexceptlist'] = None