def _new_stream(self):
    try:
        next_stream = six.advance_iterator(self.stream_generator_)
    except StopIteration:
        if self.mode == 'cycle':
            self.stream_generator_ = self.chain_streamer_.iterate()
            next_stream = six.advance_iterator(self.stream_generator_)
        else:
            next_stream = None
    if next_stream is not None:
        streamer = next_stream.iterate()
        self.streams_[0] = streamer
        self.stream_counts_[0] = 0