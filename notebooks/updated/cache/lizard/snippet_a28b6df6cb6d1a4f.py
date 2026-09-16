def perform(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((self.host, self.port))
    if not self.query:
        sock.close()
        return True
    try:
        sock.sendall(self.query)
    except Exception:
        logger.exception('Error sending TCP query message.')
        sock.close()
        return False
    response, extra = sockutils.get_response(sock)
    logger.debug('response: %s (extra: %s)', response, extra)
    if response != self.expected_response:
        logger.warn('Response does not match expected value: %s (expected %s)',
            response, self.expected_response)
        sock.close()
        return False
    sock.close()
    return True