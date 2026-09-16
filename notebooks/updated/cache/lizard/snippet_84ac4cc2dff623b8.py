def open_interface_async(self, conn_id, interface, callback,
    connection_string=None):
    if interface not in {'rpc', 'script', 'streaming', 'tracing', 'debug'}:
        callback(conn_id, self.id, False,
            'invalid interface name in call to open_interface_async')
        return
    if interface == 'rpc':
        self._open_rpc_interface(conn_id, callback)
    elif interface == 'script':
        self._open_script_interface(conn_id, callback)
    elif interface == 'streaming':
        self._open_streaming_interface(conn_id, callback)
    elif interface == 'tracing':
        self._open_tracing_interface(conn_id, callback)
    elif interface == 'debug':
        self._open_debug_interface(conn_id, callback, connection_string)
    else:
        callback(conn_id, self.id, False, 'interface not supported yet')