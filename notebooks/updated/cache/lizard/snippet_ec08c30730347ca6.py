def proxy_it(request, port):
    websocket_proxy = request.registry.settings.get(
        'pyramid_notebook.websocket_proxy', '')
    if websocket_proxy.strip():
        r = DottedNameResolver()
        websocket_proxy = r.maybe_resolve(websocket_proxy)
    if 'upgrade' in request.headers.get('connection', '').lower():
        if websocket_proxy:
            return websocket_proxy(request, port)
        else:
            raise RuntimeError('Websocket proxy support is not configured.')
    proxy_app = WSGIProxyApplication(port)
    return request.get_response(proxy_app)