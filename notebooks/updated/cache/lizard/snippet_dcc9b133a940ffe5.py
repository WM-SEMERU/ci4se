def block(self, signals=None, isBlocked=True):
    if signals:
        try:
            if isinstance(signals, basestring):
                signals = [signals]
        except NameError:
            if isinstance(signals, str):
                signals = [signals]
    signals = signals or self.keys()
    for signal in signals:
        if signal not in self:
            raise RuntimeError('Could not find signal matching %s' % signal)
        self[signal].block(isBlocked)