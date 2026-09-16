def clear(self):
    while self.current or self.idlers or self.queue or self.rpcs:
        current = self.current
        idlers = self.idlers
        queue = self.queue
        rpcs = self.rpcs
        _logging_debug('Clearing stale EventLoop instance...')
        if current:
            _logging_debug('  current = %s', current)
        if idlers:
            _logging_debug('  idlers = %s', idlers)
        if queue:
            _logging_debug('  queue = %s', queue)
        if rpcs:
            _logging_debug('  rpcs = %s', rpcs)
        self.__init__()
        current.clear()
        idlers.clear()
        queue[:] = []
        rpcs.clear()
        _logging_debug('Cleared')