def http_request(self, path, method='GET', content=None, content_type=
    'application/json', response_format=FMT_JSON):
    imeth = None
    if not method in METHMAP:
        raise E.ArgumentError.pyexc('Unknown HTTP Method', method)
    imeth = METHMAP[method]
    return self._http_request(type=LCB.LCB_HTTP_TYPE_MANAGEMENT, path=path,
        method=imeth, content_type=content_type, post_data=content,
        response_format=response_format)