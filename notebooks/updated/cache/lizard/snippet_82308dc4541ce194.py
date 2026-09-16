def _get_method(self, rdata):
    if 'method' in rdata:
        if not isinstance(rdata['method'], basestring):
            raise InvalidRequestError
    else:
        raise InvalidRequestError
    if rdata['method'] not in self.method_data.keys():
        raise MethodNotFoundError
    return rdata['method']