def put(self, message):
    header = self.HEADER_FORMAT.format(len(message))
    full_message = header + message
    sent_count = 0
    while sent_count < len(full_message):
        try:
            msg = full_message[sent_count:]
            msg = msg.encode() if self._encode else msg
            count = self._sock.send(msg)
        except socket.error as err:
            print('error')
            return False
        if count == 0:
            return False
        sent_count += count
    return True