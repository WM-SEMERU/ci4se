def observe(self, path, callback, timeout=None, **kwargs):
    request = self.mk_request(defines.Codes.GET, path)
    request.observe = 0
    for k, v in kwargs.items():
        if hasattr(request, k):
            setattr(request, k, v)
    return self.send_request(request, callback, timeout)