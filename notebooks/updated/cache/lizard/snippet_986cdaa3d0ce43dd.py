def raise_exception(self, original_exception=None):
    if self._executed_retries < self._max_retries:
        curr_backoff = self._ms_backoff
        self._executed_retries += 1
        self._ms_backoff = self._ms_backoff * 2
        raise ActionRetryException(curr_backoff)
    else:
        raise (original_exception or Exception())