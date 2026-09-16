def _checkReturnTo(self, message, return_to):
    try:
        self._verifyReturnToArgs(message.toPostArgs())
    except ProtocolError as why:
        logging.exception('Verifying return_to arguments: %s' % (why,))
        return False
    msg_return_to = message.getArg(OPENID_NS, 'return_to')
    app_parts = urlparse(urinorm.urinorm(return_to))
    msg_parts = urlparse(urinorm.urinorm(msg_return_to))
    for part in range(0, 3):
        if app_parts[part] != msg_parts[part]:
            return False
    return True