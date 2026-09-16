def set_status(self, status: Status, increment_try_count: bool=True,
    filename: str=None):
    url = self.url_record.url
    assert not self._try_count_incremented, (url, status)
    if increment_try_count:
        self._try_count_incremented = True
    _logger.debug(__('Marking URL {0} status {1}.', url, status))
    url_result = URLResult()
    url_result.filename = filename
    self.app_session.factory['URLTable'].check_in(url, status,
        increment_try_count=increment_try_count, url_result=url_result)
    self._processed = True