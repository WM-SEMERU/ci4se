def purge_all(self, remove_definitions=False):
    for stream_id in list(self.streams.keys()):
        self.purge_stream(stream_id, remove_definition=remove_definitions)