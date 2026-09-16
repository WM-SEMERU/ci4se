def scale(self, service, count=None, delta=None, **kwargs):
    if 'instances' in kwargs:
        count = kwargs.pop('instances')
        warnings.warn('instances is deprecated, use count instead')
    assert not kwargs
    if count is not None and delta is not None:
        raise context.ValueError('cannot specify both `count` and `delta`')
    elif count is None and delta is None:
        raise context.ValueError('must specify either `count` or `delta`')
    if count and count < 0:
        raise context.ValueError('count must be >= 0')
    req = proto.ScaleRequest(service_name=service, count=count, delta=delta)
    resp = self._call('scale', req)
    return [Container.from_protobuf(c) for c in resp.containers]