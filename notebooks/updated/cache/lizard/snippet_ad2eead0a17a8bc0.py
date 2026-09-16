def channels(self):
    if hasattr(self, 'pce_channels'):
        return self.pce_channels
    conf = getattr(self, 'extensionChannelConfiguration', self.
        channelConfiguration)
    if conf == 1:
        if self.psPresentFlag == -1:
            return 0
        elif self.psPresentFlag == 1:
            return 2
        else:
            return 1
    elif conf == 7:
        return 8
    elif conf > 7:
        return 0
    else:
        return conf