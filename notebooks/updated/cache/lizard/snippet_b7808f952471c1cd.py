def translate_kwargs(self, **kwargs):
    local_kwargs = self.kwargs.copy()
    local_kwargs.update(kwargs)
    if 'data' in local_kwargs and 'json' in local_kwargs:
        raise ValueError('Cannot use data and json together')
    if 'data' in local_kwargs and isinstance(local_kwargs['data'], dict):
        local_kwargs.update({'json': local_kwargs['data']})
        del local_kwargs['data']
    headers = DEFAULT_HEADERS.copy()
    if 'headers' in kwargs:
        headers.update(kwargs['headers'])
    if 'json' in local_kwargs:
        headers.update({'Content-Type': 'application/json;charset=UTF-8'})
    local_kwargs.update({'headers': headers})
    return local_kwargs