def set_header_s(self, stream):
    if self.argstreams[1].state == StreamState.init:
        self.argstreams[1] = stream
    else:
        raise TChannelError(
            'Unable to change the header since the streaming has started')