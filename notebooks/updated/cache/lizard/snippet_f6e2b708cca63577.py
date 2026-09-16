def my_protocol_parser(out, buf):
    while True:
        tp = yield from buf.read(5)
        if tp in (MSG_PING, MSG_PONG):
            yield from buf.skipuntil(b'\r\n')
            out.feed_data(Message(tp, None))
        elif tp == MSG_STOP:
            out.feed_data(Message(tp, None))
        elif tp == MSG_TEXT:
            text = yield from buf.readuntil(b'\r\n')
            out.feed_data(Message(tp, text.strip().decode('utf-8')))
        else:
            raise ValueError('Unknown protocol prefix.')