def generate_prepared_request(method, url, headers, data, params, handlers):
    request = Request(method=method, url=url, headers=headers, data=data,
        params=params)
    handlers.append(error_handler)
    for handler in handlers:
        request.register_hook('response', handler)
    return request.prepare()