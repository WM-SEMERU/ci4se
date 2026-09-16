def signals(self, signals=('QUIT', 'USR1', 'USR2')):
    for sig in signals:
        signal.signal(getattr(signal, 'SIG' + sig), self.handler)