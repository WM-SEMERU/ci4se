def connect(self, callback=None, timeout=None):
    if hasattr(self, '_connecting_future'
        ) and not self._connecting_future.done():
        future = self._connecting_future
    else:
        if hasattr(self, '_connecting_future'):
            self._connecting_future.exception()
        future = tornado.concurrent.Future()
        self._connecting_future = future
        self._connect(timeout=timeout)
    if callback is not None:

        def handle_future(future):
            response = future.result()
            self.io_loop.add_callback(callback, response)
        future.add_done_callback(handle_future)
    return future