def _wrap_callback_errors(callback, message):
    try:
        callback(message)
    except Exception:
        _LOGGER.exception(
            'Top-level exception occurred in callback while processing a message'
            )
        message.nack()