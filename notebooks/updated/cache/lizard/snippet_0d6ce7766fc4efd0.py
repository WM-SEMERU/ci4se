def on_msg(self, callback, remove=False):
    self._msg_callbacks.register_callback(callback, remove=remove)