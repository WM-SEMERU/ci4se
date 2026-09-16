def get(self, path, params=None):
    resp = self._session.get(path, params=params)
    if resp.status_code != 200:
        if resp.headers.get('Content-Type', '').startswith('text/html'):
            text = resp.reason
        else:
            text = resp.text
        raise requests.HTTPError(
            'Error accessing {0}\nServer Error ({1:d}: {2})'.format(resp.
            request.url, resp.status_code, text))
    return resp