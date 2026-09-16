async def start_pipe_server(client_connected_cb, *, path, loop=None, limit=
    DEFAULT_LIMIT):
    path = path.replace('/', '\\')
    loop = loop or asyncio.get_event_loop()

    def factory():
        reader = asyncio.StreamReader(limit=limit, loop=loop)
        protocol = asyncio.StreamReaderProtocol(reader, client_connected_cb,
            loop=loop)
        return protocol
    server, *_ = await loop.start_serving_pipe(factory, address=path)
    closed = asyncio.Event(loop=loop)
    original_close = server.close

    def close():
        original_close()
        closed.set()
    server.close = close
    server.wait_closed = closed.wait
    return server