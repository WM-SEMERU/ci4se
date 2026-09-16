def url(self):
    local_path = self._find_in_local()
    if local_path:
        return local_path
    if not self._url:
        self._refresh_url()
    elif time.time() > self._expired_at:
        logger.info('song({}) url is expired, refresh...'.format(self))
        self._refresh_url()
    return self._url