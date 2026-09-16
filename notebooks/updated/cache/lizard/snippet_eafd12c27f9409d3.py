def _get_request_args(method, **kwargs):
    args = [('api_key', api_key), ('format', 'json'), ('method', method), (
        'nojsoncallback', '1')]
    if kwargs:
        for key, value in kwargs.iteritems():
            args.append((key, value))
    args.sort(key=lambda tup: tup[0])
    api_sig = _get_api_sig(args)
    args.append(api_sig)
    return args