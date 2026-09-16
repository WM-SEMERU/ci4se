def curlrequests(curl_string, **kwargs):
    req = kwargs.pop('req', tPool())
    kwargs.update(curlparse(curl_string))
    return req.request(**kwargs)