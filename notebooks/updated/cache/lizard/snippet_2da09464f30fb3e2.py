def disconnect_async(self, conn_id, callback):
    future = self._loop.launch_coroutine(self._adapter.disconnect(conn_id))
    future.add_done_callback(lambda x: self._callback_future(conn_id, x,
        callback))