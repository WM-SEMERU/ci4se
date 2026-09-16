def execute(self, command, *args, encoding=_NOTSET):
    if self._reader is None or self._reader.at_eof():
        msg = self._close_msg or 'Connection closed or corrupted'
        raise ConnectionClosedError(msg)
    if command is None:
        raise TypeError('command must not be None')
    if None in args:
        raise TypeError('args must not contain None')
    command = command.upper().strip()
    is_pubsub = command in _PUBSUB_COMMANDS
    is_ping = command in ('PING', b'PING')
    if self._in_pubsub and not (is_pubsub or is_ping):
        raise RedisError('Connection in SUBSCRIBE mode')
    elif is_pubsub:
        logger.warning('Deprecated. Use `execute_pubsub` method directly')
        return self.execute_pubsub(command, *args)
    if command in ('SELECT', b'SELECT'):
        cb = partial(self._set_db, args=args)
    elif command in ('MULTI', b'MULTI'):
        cb = self._start_transaction
    elif command in ('EXEC', b'EXEC'):
        cb = partial(self._end_transaction, discard=False)
    elif command in ('DISCARD', b'DISCARD'):
        cb = partial(self._end_transaction, discard=True)
    else:
        cb = None
    if encoding is _NOTSET:
        encoding = self._encoding
    fut = self._loop.create_future()
    if self._pipeline_buffer is None:
        self._writer.write(encode_command(command, *args))
    else:
        encode_command(command, *args, buf=self._pipeline_buffer)
    self._waiters.append((fut, encoding, cb))
    return fut