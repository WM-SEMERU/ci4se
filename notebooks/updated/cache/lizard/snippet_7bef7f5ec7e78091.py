def maybe_expire(self, request_timeout_ms, retry_backoff_ms, linger_ms, is_full
    ):
    now = time.time()
    since_append = now - self.last_append
    since_ready = now - (self.created + linger_ms / 1000.0)
    since_backoff = now - (self.last_attempt + retry_backoff_ms / 1000.0)
    timeout = request_timeout_ms / 1000.0
    error = None
    if not self.in_retry() and is_full and timeout < since_append:
        error = '%d seconds have passed since last append' % (since_append,)
    elif not self.in_retry() and timeout < since_ready:
        error = (
            '%d seconds have passed since batch creation plus linger time' %
            (since_ready,))
    elif self.in_retry() and timeout < since_backoff:
        error = (
            '%d seconds have passed since last attempt plus backoff time' %
            (since_backoff,))
    if error:
        self.records.close()
        self.done(-1, None, Errors.KafkaTimeoutError(
            'Batch for %s containing %s record(s) expired: %s' % (self.
            topic_partition, self.records.next_offset(), error)))
        return True
    return False