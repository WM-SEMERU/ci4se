def stop(self):
    logger.debug('Stopping')
    self._closing = True
    self.stop_consuming()
    self._connection.ioloop.start()
    logger.debug('Stopped')