def send(self):
    import requests
    if not self._is_enabled():
        return
    self.collect()
    logger.debug('Sending analytics: {}'.format(self.info))
    try:
        requests.post(self.URL, json=self.info, timeout=self.TIMEOUT_POST)
    except requests.exceptions.RequestException as exc:
        logger.debug('Failed to send analytics: {}'.format(str(exc)))