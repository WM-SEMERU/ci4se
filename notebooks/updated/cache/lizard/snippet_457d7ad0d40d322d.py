async def create_tunnel_connection(self, req):
    tunnel_address = req.tunnel_address
    connection = await self.create_connection(tunnel_address)
    response = connection.current_consumer()
    for event in response.events().values():
        event.clear()
    response.start(HttpTunnel(self, req))
    await response.event('post_request').waiter()
    if response.status_code != 200:
        raise ConnectionRefusedError(
            'Cannot connect to tunnel: status code %s' % response.status_code)
    raw_sock = connection.transport.get_extra_info('socket')
    if raw_sock is None:
        raise RuntimeError('Transport without socket')
    raw_sock = raw_sock.dup()
    connection.transport.close()
    await connection.event('connection_lost').waiter()
    self.sessions -= 1
    self.requests_processed -= 1
    connection = await self.create_connection(sock=raw_sock, ssl=req.ssl(
        self), server_hostname=req.netloc)
    return connection