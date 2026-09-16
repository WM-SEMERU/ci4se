def processRequest(cls, ps, **kw):
    resource = kw['resource']
    method = resource.getOperation(ps, None)
    rsp = method(ps, **kw)[1]
    return rsp