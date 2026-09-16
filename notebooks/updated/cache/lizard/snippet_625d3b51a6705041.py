def start(self):
    if threading.current_thread().name == 'MainThread':
        signal.signal(signal.SIGINT, self.stop)
    logging.info('Started on {}'.format(self.address))
    while True:
        self.process()