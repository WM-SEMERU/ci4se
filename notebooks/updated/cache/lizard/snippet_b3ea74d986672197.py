def _get_nonce(self, url):
    action = LOG_JWS_GET_NONCE()
    if len(self._nonces) > 0:
        with action:
            nonce = self._nonces.pop()
            action.add_success_fields(nonce=nonce)
            return succeed(nonce)
    else:
        with action.context():
            return DeferredContext(self.head(url)).addCallback(self._add_nonce
                ).addCallback(lambda _: self._nonces.pop()).addCallback(tap
                (lambda nonce: action.add_success_fields(nonce=nonce))
                ).addActionFinish()