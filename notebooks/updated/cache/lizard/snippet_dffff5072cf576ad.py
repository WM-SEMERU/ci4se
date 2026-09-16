def process(self, session: AppSession):
    args = session.args
    if not (args.phantomjs or args.youtube_dl or args.proxy_server):
        return
    proxy_server = session.factory.new('HTTPProxyServer', session.factory[
        'HTTPClient'])
    cookie_jar = session.factory.get('CookieJarWrapper')
    proxy_coprocessor = session.factory.new('ProxyCoprocessor', session)
    proxy_socket = tornado.netutil.bind_sockets(session.args.
        proxy_server_port, address=session.args.proxy_server_address)[0]
    proxy_port = proxy_socket.getsockname()[1]
    proxy_async_server = yield from asyncio.start_server(proxy_server, sock
        =proxy_socket)
    session.async_servers.append(proxy_async_server)
    session.proxy_server_port = proxy_port