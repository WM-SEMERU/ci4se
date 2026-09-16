async def send_async(self, message, callback, timeout=0):
    try:
        raise self._error
    except TypeError:
        pass
    except Exception as e:
        _logger.warning('%r', e)
        raise
    c_message = message.get_message()
    message._on_message_sent = callback
    try:
        await self._session._connection.lock_async(timeout=None)
        return self._sender.send(c_message, timeout, message)
    finally:
        self._session._connection.release_async()