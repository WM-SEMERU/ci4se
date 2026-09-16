def _task_periodic(self):
    log = self._params.get('log', self._discard)
    log.debug('periodic')
    self.manage()