def _register_signal_handler(self, description, signal, handler):
    from flask import signals
    if not signals.signals_available:
        self.app.logger.warn(
            'blinker needs to be installed in order to support %s'.format(
            description))
    self.app.logger.info('Enabling {}'.format(description))
    signal.connect(handler, sender=self.app, weak=False)