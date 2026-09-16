def make_batched_timer(self, bucket_seconds, chunk_size=100):

    def get_seconds():
        return self._get_loop().seconds()

    def create_delayed_call(delay, fun, *args, **kwargs):
        return self._get_loop().callLater(delay, fun, *args, **kwargs)
    return _BatchedTimer(bucket_seconds * 1000.0, chunk_size,
        seconds_provider=get_seconds, delayed_call_creator=create_delayed_call)