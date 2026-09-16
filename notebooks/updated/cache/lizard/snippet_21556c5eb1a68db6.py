def get_url_preview(self, url, ts=None):
    params = {'url': url}
    if ts:
        params['ts'] = ts
    return self._send('GET', '', query_params=params, api_path=
        '/_matrix/media/r0/preview_url')