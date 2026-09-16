def next_event(self):
    if self.their_state is ERROR:
        raise RemoteProtocolError("Can't receive data when peer state is ERROR"
            )
    try:
        event = self._extract_next_receive_event()
        if event not in [NEED_DATA, PAUSED]:
            self._process_event(self.their_role, event)
            self._receive_buffer.compress()
        if event is NEED_DATA:
            if len(self._receive_buffer) > self._max_incomplete_event_size:
                raise RemoteProtocolError('Receive buffer too long',
                    error_status_hint=431)
            if self._receive_buffer_closed:
                raise RemoteProtocolError('peer unexpectedly closed connection'
                    )
        return event
    except BaseException as exc:
        self._process_error(self.their_role)
        if isinstance(exc, LocalProtocolError):
            exc._reraise_as_remote_protocol_error()
        else:
            raise