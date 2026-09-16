def stop(self, message):
    self._stop = time.clock()
    VSGLogger.info('{0:<20} - Finished [{1}s]'.format(message, self.pprint(
        self._stop - self._start)))