def close(self):
    if not hasattr(self, '_closed') or self._closed:
        log.info('KafkaAdminClient already closed.')
        return
    self._metrics.close()
    self._client.close()
    self._closed = True
    log.debug('KafkaAdminClient is now closed.')