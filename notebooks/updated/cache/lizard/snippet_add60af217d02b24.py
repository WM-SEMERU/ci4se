def show_app(app, state, notebook_url, port=0, **kw):
    logging.basicConfig()
    from tornado.ioloop import IOLoop
    from ..server.server import Server
    loop = IOLoop.current()
    if callable(notebook_url):
        origin = notebook_url(None)
    else:
        origin = _origin_url(notebook_url)
    server = Server({'/': app}, io_loop=loop, port=port,
        allow_websocket_origin=[origin], **kw)
    server_id = uuid4().hex
    curstate().uuid_to_server[server_id] = server
    server.start()
    if callable(notebook_url):
        url = notebook_url(server.port)
    else:
        url = _server_url(notebook_url, server.port)
    logging.debug('Server URL is %s' % url)
    logging.debug('Origin URL is %s' % origin)
    from ..embed import server_document
    script = server_document(url, resources=None)
    publish_display_data({HTML_MIME_TYPE: script, EXEC_MIME_TYPE: ''},
        metadata={EXEC_MIME_TYPE: {'server_id': server_id}})