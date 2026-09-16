def _init_handler(self, session, reader, writer):
    handler = BrokerProtocolHandler(self.plugins_manager, self._loop)
    handler.attach(session, reader, writer)
    return handler