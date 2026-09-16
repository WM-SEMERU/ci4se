def connect_async(self, conn_id, connection_string, callback):
    future = self._loop.launch_coroutine(self._adapter.connect(conn_id,
        connection_string))
    future.add_done_callback(lambda x: self._callback_future(conn_id, x,
        callback))