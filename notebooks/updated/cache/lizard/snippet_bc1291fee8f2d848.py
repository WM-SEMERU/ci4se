def handle_connection(stream):
    ws = WSConnection(ConnectionType.SERVER)
    events = ws.events()
    running = True
    while running:
        in_data = stream.recv(RECEIVE_BYTES)
        print('Received {} bytes'.format(len(in_data)))
        ws.receive_data(in_data)
        try:
            event = next(events)
        except StopIteration:
            print('Client connection dropped unexpectedly')
            return
        if isinstance(event, Request):
            print('Accepting WebSocket upgrade')
            out_data = ws.send(AcceptConnection())
        elif isinstance(event, CloseConnection):
            print('Connection closed: code={}/{} reason={}'.format(event.
                code.value, event.code.name, event.reason))
            out_data = ws.send(event.response())
            running = False
        elif isinstance(event, TextMessage):
            print('Received request and sending response')
            out_data = ws.send(Message(data=event.data[::-1]))
        elif isinstance(event, Ping):
            print('Received ping and sending pong')
            out_data = ws.send(event.response())
        else:
            print('Unknown event: {!r}'.format(event))
        print('Sending {} bytes'.format(len(out_data)))
        stream.send(out_data)