def handle_end_signal(self):
    try:
        signal.signal(signal.SIGTERM, self.catch_end_signal)
        signal.signal(signal.SIGINT, self.catch_end_signal)
    except ValueError:
        self.log('Signals cannot be caught in a Thread', level='warning')