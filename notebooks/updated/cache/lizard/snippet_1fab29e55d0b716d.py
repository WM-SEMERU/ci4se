def process(self):
    log.debug('Processing drawing')
    with self._cache:
        for func in self._process_functions():
            func()
    return self