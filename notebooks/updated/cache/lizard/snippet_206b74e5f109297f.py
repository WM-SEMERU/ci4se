def get_cdn_metadata(self, container):
    uri = '%s/%s' % (self.uri_base, utils.get_name(container))
    resp, resp_body = self.api.cdn_request(uri, 'HEAD')
    ret = dict(resp.headers)
    ret.pop('content-length', None)
    ret.pop('content-type', None)
    ret.pop('date', None)
    return ret