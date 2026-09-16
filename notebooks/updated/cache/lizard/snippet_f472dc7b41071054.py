def wait_for(self, wait_for, timeout_ms):
    if not isinstance(wait_for, baseinteger):
        raise TypeError('wait_for can only be an instance of type baseinteger')
    if not isinstance(timeout_ms, baseinteger):
        raise TypeError(
            'timeout_ms can only be an instance of type baseinteger')
    reason = self._call('waitFor', in_p=[wait_for, timeout_ms])
    reason = ProcessWaitResult(reason)
    return reason