def _read_msg_header(session):
    try:
        data = session.socket.recv(6 - len(session.data))
        if len(data) == 0:
            return NO_DATA
        session.data += data
        if len(session.data) < 6:
            return INCOMPLETE
    except ssl.SSLError:
        return INCOMPLETE
    session.message_length = struct.unpack('!i', session.data[2:6])[0]
    response_type = struct.unpack('!H', session.data[0:2])[0]
    session.data = six.b('')
    return response_type