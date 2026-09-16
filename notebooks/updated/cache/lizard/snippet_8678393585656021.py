def get_webpack(request, name='DEFAULT'):
    if not hasattr(request, '_webpack_map'):
        request._webpack_map = {}
    wp = request._webpack_map.get(name)
    if wp is None:
        wp = request._webpack_map[name] = Webpack(request, name)
    return wp