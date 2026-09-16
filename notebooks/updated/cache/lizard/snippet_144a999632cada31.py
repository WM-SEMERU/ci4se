async def recv_initial_metadata(self):
    if not self._send_request_done:
        raise ProtocolError('Request was not sent yet')
    if self._recv_initial_metadata_done:
        raise ProtocolError('Initial metadata was already received')
    try:
        with self._wrapper:
            headers = await self._stream.recv_headers()
            self._recv_initial_metadata_done = True
            metadata = decode_metadata(headers)
            metadata, = await self._dispatch.recv_initial_metadata(metadata)
            self.initial_metadata = metadata
            headers_map = dict(headers)
            self._raise_for_status(headers_map)
            self._raise_for_grpc_status(headers_map, optional=True)
            content_type = headers_map.get('content-type')
            if content_type is None:
                raise GRPCError(Status.UNKNOWN, 'Missing content-type header')
            base_content_type, _, sub_type = content_type.partition('+')
            sub_type = sub_type or ProtoCodec.__content_subtype__
            if (base_content_type != GRPC_CONTENT_TYPE or sub_type != self.
                _codec.__content_subtype__):
                raise GRPCError(Status.UNKNOWN,
                    'Invalid content-type: {!r}'.format(content_type))
    except StreamTerminatedError:
        headers = self._stream.recv_headers_nowait()
        if headers is None:
            raise
        else:
            headers_map = dict(headers)
            self._raise_for_status(headers_map)
            self._raise_for_grpc_status(headers_map, optional=True)
            raise