def request(self, method, uri, **kwargs):
    response = self.raw_request(method, uri, **kwargs)
    if response.status_code != 200:
        exception_class = HTTP_STATUS_EXCEPTION_MAP.get(response.
            status_code, WVAHttpError)
        raise exception_class(response)
    if response.headers.get('content-type') == 'application/json':
        return json.loads(response.text)
    else:
        return response.text