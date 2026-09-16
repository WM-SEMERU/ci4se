def close(self):
    self._closed = True
    if self.receive_task:
        self.receive_task.cancel()
    if self.connection:
        self.connection.close()