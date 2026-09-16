def stop(self):
    LOG.info('Shutting down server')
    self.server.shutdown()
    LOG.debug('ServerThread.stop: Stopping ServerThread')
    self.server.server_close()
    LOG.info('Server stopped')