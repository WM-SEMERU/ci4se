def all_of(api_call, *args, **kwargs):
    kwargs = kwargs.copy()
    pos, outer_limit = 0, kwargs.get('limit', 0) or sys.maxsize
    while True:
        response = api_call(*args, **kwargs)
        for item in response.get('results', []):
            pos += 1
            if pos > outer_limit:
                return
            yield item
        if response.get('_links', {}).get('next', None):
            kwargs['start'] = response['start'] + response['size']
            kwargs['limit'] = response['limit']
        else:
            return