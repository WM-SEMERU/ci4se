def create_stream(self, stream_id, sandbox=None):
    if stream_id in self.streams:
        raise StreamAlreadyExistsError("Stream with id '{}' already exists"
            .format(stream_id))
    if sandbox is not None:
        raise ValueError('Cannot use sandboxes with memory streams')
    stream = Stream(channel=self, stream_id=stream_id, calculated_intervals
        =None, sandbox=None)
    self.streams[stream_id] = stream
    self.data[stream_id] = StreamInstanceCollection()
    return stream