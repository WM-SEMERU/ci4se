def stop(self):
    for s in self._servers:
        s.stop()
    for g in self._server_greenlets:
        g.kill()
    logger.info('All workers stopped.')