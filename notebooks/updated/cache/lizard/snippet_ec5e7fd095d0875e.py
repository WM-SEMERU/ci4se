def head(self, req_and_resp, **kwargs):
    opt = kwargs.pop('opt', {})
    req_and_resp[0].reset()
    req_and_resp[1].reset()
    request, response = super(EsiClient, self).request(req_and_resp, opt)
    res = self.__make_request(request, opt, method='HEAD')
    response.apply_with(status=res.status_code, header=res.headers, raw=None)
    if 'warning' in res.headers:
        LOGGER.warning('[%s] %s', res.url, res.headers['warning'])
        warnings.warn('[%s] %s' % (res.url, res.headers['warning']))
    if res.status_code >= 400 and kwargs.pop('raise_on_error', False):
        raise APIException(request.url, res.status_code, response='',
            request_param=request.query, response_header=response.header)
    return response