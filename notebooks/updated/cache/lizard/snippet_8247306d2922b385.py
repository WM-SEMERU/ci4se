def recv_raw(self, timeout, opcodes, **kwargs):
    orig_timeout = self.get_timeout(timeout)
    timeout = orig_timeout
    while timeout > 0.0:
        start = time.time()
        if not self.connected:
            self.connect(timeout=timeout, **kwargs)
        with self.wstimeout(timeout, **kwargs) as timeout:
            logger.debug('{} waiting to receive for {} seconds'.format(self
                .client_id, timeout))
            try:
                opcode, data = self.ws.recv_data()
                if opcode in opcodes:
                    timeout = 0.0
                    break
                elif opcode == websocket.ABNF.OPCODE_CLOSE:
                    raise websocket.WebSocketConnectionClosedException()
            except websocket.WebSocketTimeoutException:
                pass
            except websocket.WebSocketConnectionClosedException:
                try:
                    self.ws.shutdown()
                except AttributeError:
                    pass
        if timeout:
            stop = time.time()
            timeout -= stop - start
        else:
            break
    if timeout < 0.0:
        raise IOError('recv timed out in {} seconds'.format(orig_timeout))
    return opcode, data