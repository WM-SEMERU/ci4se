def Clear(self):
    headers = {'Content-length': '0'}
    response, _ = self._http.request('%s/reset' % self._host, method='POST',
        headers=headers)
    if response.status == 200:
        return True
    else:
        logging.warning('failed to clear emulator; response was: %s', response)