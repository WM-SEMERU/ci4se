def iterintervals(self, n=2):
    streams = tee(iter(self), n)
    for stream_index, stream in enumerate(streams):
        for i in range(stream_index):
            next(stream)
    for intervals in zip(*streams):
        yield intervals