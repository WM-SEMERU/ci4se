def send(self, conn):
    if conn is None:
        raise ValueError('Cannot send to connection None')
    with (yield conn.write_lock.acquire()):
        sent = 0
        yield conn.write_message(self.header_json, locked=False)
        sent += len(self.header_json)
        yield conn.write_message(self.metadata_json, locked=False)
        sent += len(self.metadata_json)
        yield conn.write_message(self.content_json, locked=False)
        sent += len(self.content_json)
        sent += yield self.write_buffers(conn, locked=False)
        raise gen.Return(sent)