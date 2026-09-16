def request(self, method, url, data=None, files=None, query=None, headers=
    None, timeout=60):
    headers = headers or {}
    if self.token:
        my_token = self.token
    else:
        from figure import token
        my_token = token
    if my_token:
        self.__set_authorization(headers, my_token)
    METHODS = {'get': self.__get, 'post': self.__post, 'put': self.__put,
        'head': self.__head, 'patch': self.__patch}
    request_method = METHODS[method.lower()]
    abs_url = urlparse.urljoin(self.api_base, url)
    encoded_query = urllib.urlencode(query or {})
    abs_url = _build_api_url(abs_url, encoded_query)
    try:
        response = request_method(abs_url, data=data, files=files, headers=
            headers, timeout=timeout)
        response.encoding = 'utf-8'
    except RequestException:
        raise error.APIConnectionError()
    return self._interpret_response(response.text, response.status_code)