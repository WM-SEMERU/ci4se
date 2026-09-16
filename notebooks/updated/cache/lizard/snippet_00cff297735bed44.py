def _apply_callback(cls, callback, result):
    if not callback.immutable:
        callback.args = (result.id,) + callback.args
    callback.apply()