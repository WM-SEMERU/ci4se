def _LoadInternal(self):
    if not self._loader:
        self._InitializeLoader()
    while True:
        for event in self._loader.Load():
            yield event
        next_path = self._GetNextPath()
        if not next_path:
            logger.info('No path found after %s', self._path)
            return
        for event in self._loader.Load():
            yield event
        logger.info('Directory watcher advancing from %s to %s', self._path,
            next_path)
        self._SetPath(next_path)