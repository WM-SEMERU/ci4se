def close(self):
    self.application.client_leaving(self)
    self.conn.close()
    self.closed = True