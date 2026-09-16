def _retrieve_offsets(self, timestamps, timeout_ms=float('inf')):
    if not timestamps:
        return {}
    start_time = time.time()
    remaining_ms = timeout_ms
    while remaining_ms > 0:
        future = self._send_offset_requests(timestamps)
        self._client.poll(future=future, timeout_ms=remaining_ms)
        if future.succeeded():
            return future.value
        if not future.retriable():
            raise future.exception
        elapsed_ms = (time.time() - start_time) * 1000
        remaining_ms = timeout_ms - elapsed_ms
        if remaining_ms < 0:
            break
        if future.exception.invalid_metadata:
            refresh_future = self._client.cluster.request_update()
            self._client.poll(future=refresh_future, timeout_ms=remaining_ms)
        else:
            time.sleep(self.config['retry_backoff_ms'] / 1000.0)
        elapsed_ms = (time.time() - start_time) * 1000
        remaining_ms = timeout_ms - elapsed_ms
    raise Errors.KafkaTimeoutError(
        'Failed to get offsets by timestamps in %s ms' % (timeout_ms,))