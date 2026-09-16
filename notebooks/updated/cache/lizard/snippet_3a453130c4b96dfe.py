def send_rpc_async(self, conn_id, address, rpc_id, payload, timeout, callback):
    found_handle = None
    for handle, conn in self._connections.items():
        if conn['connection_id'] == conn_id:
            found_handle = handle
    if found_handle is None:
        callback(conn_id, self.id, False, 'Invalid connection_id', None, None)
        return
    services = self._connections[found_handle]['services']
    self._command_task.async_command(['_send_rpc', found_handle, services,
        address, rpc_id, payload, timeout], self._send_rpc_finished, {
        'connection_id': conn_id, 'handle': found_handle, 'callback': callback}
        )