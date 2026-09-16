def redirect(self, url):
    new_request = self._parse_request(url=url, handle=self.request.handle)
    log.debug('Redirecting %s to %s', self.request.path, new_request.path)
    return self._dispatch(new_request.path)