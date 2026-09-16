def wait(self, timeout=None):
    if threadable.isInIOThread():
        raise RuntimeError(
            'EventualResult.wait() must not be run in the reactor thread.')
    if imp.lock_held():
        try:
            imp.release_lock()
        except RuntimeError:
            pass
        else:
            raise RuntimeError(
                'EventualResult.wait() must not be run at module import time.')
    result = self._result(timeout)
    if isinstance(result, Failure):
        result.raiseException()
    return result