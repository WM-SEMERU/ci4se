def _get_http_args(self, params):
    headers = self.http_args.get('headers', {})
    if self.auth is not None:
        auth_headers = self.auth.get_headers()
        headers.update(auth_headers)
    http_args = self.http_args.copy()
    if self._source_id is not None:
        headers['source_id'] = self._source_id
    http_args['headers'] = headers
    merged_params = http_args.get('params', {})
    merged_params.update(params)
    http_args['params'] = merged_params
    return http_args