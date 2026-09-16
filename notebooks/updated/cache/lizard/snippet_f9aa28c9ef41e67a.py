def setup(self, environ):
    request = wsgi_request(environ)
    cfg = request.cache.cfg
    loop = request.cache._loop
    self.store = create_store(cfg.data_store, loop=loop)
    pubsub = self.store.pubsub(protocol=Protocol())
    channel = '%s_webchat' % self.name
    ensure_future(pubsub.subscribe(channel), loop=loop)
    return WsgiHandler([Router('/', get=self.home_page), WebSocket(
        '/message', Chat(pubsub, channel)), Router('/rpc', post=Rpc(pubsub,
        channel), response_content_types=JSON_CONTENT_TYPES)], [
        AsyncResponseMiddleware, GZipMiddleware(min_length=20)])