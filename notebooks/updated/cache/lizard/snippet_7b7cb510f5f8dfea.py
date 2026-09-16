def post(self, url, headers=None, data=None, timeout=None):
    if timeout is None:
        timeout = self.timeout
    response = requests.post(url, headers=headers, data=data, timeout=timeout)
    return RequestsHttpResponse(response)