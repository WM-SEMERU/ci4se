def pause_with_reason(self, reason):
    if not isinstance(reason, Reason):
        raise TypeError('reason can only be an instance of type Reason')
    self._call('pauseWithReason', in_p=[reason])