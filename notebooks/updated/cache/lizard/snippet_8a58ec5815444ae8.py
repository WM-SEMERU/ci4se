def create_healthcheck(self, service_id, version_number, name, host, method
    ='HEAD', path='/', http_version='1.1', timeout=1000, check_interval=
    5000, expected_response=200, window=5, threshold=3, initial=1):
    body = self._formdata({'name': name, 'method': method, 'host': host,
        'path': path, 'http_version': http_version, 'timeout': timeout,
        'check_interval': check_interval, 'expected_response':
        expected_response, 'window': window, 'threshold': threshold,
        'initial': initial}, FastlyHealthCheck.FIELDS)
    content = self._fetch('/service/%s/version/%d/healthcheck' % (
        service_id, version_number), method='POST', body=body)
    return FastlyHealthCheck(self, content)