def _prepare_proxy(self, conn):
    conn.set_tunnel(self._proxy_host, self.port, self.proxy_headers)
    conn.connect()