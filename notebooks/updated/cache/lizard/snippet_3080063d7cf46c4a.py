def invoke(self):
    logger.debug('Running deferred function %s.', self)
    self.module.makeLoadable()
    function, args, kwargs = list(map(dill.loads, (self.function, self.args,
        self.kwargs)))
    return function(*args, **kwargs)