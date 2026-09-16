def handle_simple_responses(self, timeout_ms=None, info_cb=
    DEFAULT_MESSAGE_CALLBACK):
    return self._accept_responses('OKAY', info_cb, timeout_ms=timeout_ms)