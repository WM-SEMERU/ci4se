def debug(self, onOff, level='DEBUG'):
    if onOff:
        if level == 'DEBUG':
            self.log.setLevel(logging.DEBUG)
            self._ch.setLevel(logging.DEBUG)
            self.log.debug('Debugging level DEBUG enabled')
        elif level == 'INFO':
            self.log.setLevel(logging.INFO)
            self._ch.setLevel(logging.INFO)
            self.log.info('Debugging level INFO enabled')
        elif level == 'WARN':
            self.log.setLevel(logging.WARN)
            self._ch.setLevel(logging.WARN)
            self.log.warn('Debugging level WARN enabled')
        elif level == 'ERROR':
            self.log.setLevel(logging.ERROR)
            self._ch.setLevel(logging.ERROR)
            self.log.error('Debugging level ERROR enabled')
    else:
        self.log.setLevel(logging.ERROR)
        self._ch.setLevel(logging.ERROR)
        self.log.error(
            'Unrecognized debug level `%s`, set to default level `ERROR` instead'
            , level)