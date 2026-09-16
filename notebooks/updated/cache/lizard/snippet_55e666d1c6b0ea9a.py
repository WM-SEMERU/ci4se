def clean_headers(self):
    if not isinstance(self.request.get('headers'), dict):
        return self
    headers = self.request['headers']
    if 'Cookie' in headers:
        self.clean_cookie()
    for key in headers:
        if key == 'Cookie':
            continue
        new_request = deepcopy(self.request)
        new_headers = deepcopy(headers)
        new_headers.pop(key)
        new_request['headers'] = new_headers
        self._add_task('headers', key, new_request)
    return self