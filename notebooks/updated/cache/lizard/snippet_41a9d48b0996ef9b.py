def _subthread_handle_accepted(self, client):
    conn, addr = client
    if self.handle_incoming(conn, addr):
        logging.info('Accepted connection from client: {}'.format(addr))
        conn.setblocking(False)
        self.clients[conn] = addr
        self.register(conn)
    else:
        logging.info('Refused connection from client: {}'.format(addr))
        self.disconnect(conn)