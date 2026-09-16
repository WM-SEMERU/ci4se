def close(self):
    self.acquire()
    try:
        if self.transport is not None:
            self.transport.close()
        super(Rfc5424SysLogHandler, self).close()
    finally:
        self.release()