def _cached_results(self, start_time, end_time):
    cached_buckets = self._bucket_events(self._client.get(self.
        _scratch_stream, start_time, end_time, namespace=self.
        _scratch_namespace))
    for bucket_events in cached_buckets:
        if len(bucket_events) == 1:
            first_result = bucket_events[0]
            yield kronos_time_to_epoch_time(first_result[TIMESTAMP_FIELD]
                ), first_result[QueryCache.CACHE_KEY]