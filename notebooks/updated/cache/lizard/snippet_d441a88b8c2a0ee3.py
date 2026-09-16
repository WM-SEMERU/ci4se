def _cancel_callback(self, request_id):

    def callback(future):
        if future.cancelled():
            self.notify(CANCEL_METHOD, {'id': request_id})
            future.set_exception(JsonRpcRequestCancelled())
    return callback