def _on_connection_failed(self, conn_id, handle, clean, reason):
    with self.count_lock:
        self.connecting_count -= 1
    self._logger.info('_on_connection_failed conn_id=%d, reason=%s',
        conn_id, str(reason))
    conndata = self._get_connection(handle)
    if conndata is None:
        self._logger.info(
            'Unable to obtain connection data on unknown connection %d',
            conn_id)
        return
    callback = conndata['callback']
    conn_id = conndata['connection_id']
    failure_reason = conndata['failure_reason']
    if 'error_code' in conndata and conndata['error_code'] == 574 and conndata[
        'retries'] > 0:
        self._remove_connection(handle)
        self.connect_async(conn_id, conndata['connection_string'], callback,
            conndata['retries'] - 1)
    else:
        callback(conn_id, self.id, False, failure_reason)
        self._remove_connection(handle)