def _read_data_handler(whence, ctx, complete, can_flush):
    trans = None
    queue = ctx.queue
    while True:
        data_event, self = yield trans
        if data_event is not None:
            if data_event.data is not None:
                data = data_event.data
                data_len = len(data)
                if data_len > 0:
                    queue.extend(data)
                    yield Transition(None, whence)
            elif data_event.type is ReadEventType.NEXT:
                queue.mark_eof()
                if not can_flush:
                    _illegal_character(queue.read_byte(), ctx,
                        'Unexpected EOF.')
                yield Transition(None, whence)
        trans = Transition(complete and ION_STREAM_END_EVENT or
            ION_STREAM_INCOMPLETE_EVENT, self)