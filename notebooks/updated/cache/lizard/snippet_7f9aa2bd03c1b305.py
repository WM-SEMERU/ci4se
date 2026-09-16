def on_client_connect(self, client_conn):
    assert get_thread_ident() == self._server.ioloop_thread_id
    self._client_conns.add(client_conn)
    self._strategies[client_conn] = {}
    katcp_version = self.PROTOCOL_INFO.major
    if katcp_version >= VERSION_CONNECT_KATCP_MAJOR:
        client_conn.inform(Message.inform('version-connect',
            'katcp-protocol', self.PROTOCOL_INFO))
        client_conn.inform(Message.inform('version-connect',
            'katcp-library', 'katcp-python-%s' % katcp.__version__))
        client_conn.inform(Message.inform('version-connect', 'katcp-device',
            self.version(), self.build_state()))
    else:
        client_conn.inform(Message.inform('version', self.version()))
        client_conn.inform(Message.inform('build-state', self.build_state()))