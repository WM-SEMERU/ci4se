def shutdown(self, how):
    if how == 0 or how == 2:
        self.eof_received = 1
    if how == 1 or how == 2:
        self.lock.acquire()
        try:
            m = self._send_eof()
        finally:
            self.lock.release()
        if m is not None:
            self.transport._send_user_message(m)