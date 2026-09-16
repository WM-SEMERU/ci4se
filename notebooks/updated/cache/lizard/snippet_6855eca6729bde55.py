def getBody(cls, url, method='GET', headers={}, data=None, socket=None,
    timeout=120):
    if not 'User-Agent' in headers:
        headers['User-Agent'] = ['Tensor HTTP checker']
    return cls().request(url, method, headers, data, socket, timeout)