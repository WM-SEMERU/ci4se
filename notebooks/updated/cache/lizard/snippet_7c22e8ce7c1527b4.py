def close(self):
    scoop.logger.debug('Closing workers on {0}.'.format(self))
    for process in self.subprocesses:
        try:
            process.terminate()
        except OSError:
            pass