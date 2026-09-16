def on(self, message, namespace=None):
    namespace = namespace or '/'

    def decorator(handler):

        def _handler(sid, *args):
            return self._handle_event(handler, message, namespace, sid, *args)
        if self.server:
            self.server.on(message, _handler, namespace=namespace)
        else:
            self.handlers.append((message, _handler, namespace))
        return handler
    return decorator