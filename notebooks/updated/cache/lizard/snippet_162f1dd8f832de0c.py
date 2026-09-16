def get_or_create_stream(self, stream_id, try_create=True):
    stream_id = get_stream_id(stream_id)
    if stream_id in self.streams:
        logging.debug('found {}'.format(stream_id))
        return self.streams[stream_id]
    elif try_create:
        logging.debug('creating {}'.format(stream_id))
        return self.create_stream(stream_id=stream_id)