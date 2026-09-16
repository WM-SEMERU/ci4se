def register_iq_request_coro(self, type_, payload_cls, coro):
    warnings.warn(
        'register_iq_request_coro is a deprecated alias to register_iq_request_handler and will be removed in aioxmpp 1.0'
        , DeprecationWarning, stacklevel=2)
    return self.register_iq_request_handler(type_, payload_cls, coro)