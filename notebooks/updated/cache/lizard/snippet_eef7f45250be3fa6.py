def handle_error(self, callback):
    self.loop.log_error(callback)
    msg = '\n'.join(['Exception in callback %r' % callback, traceback.
        format_exc()])
    self.show_error(msg.encode('utf-8'))