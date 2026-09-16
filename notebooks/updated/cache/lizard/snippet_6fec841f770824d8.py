def _flusher_loop(self):
    while True:
        pending = []
        pending_size = 0
        try:
            yield self._flush_queue.get()
            if not self.is_connected or self.is_connecting or self.io.closed():
                break
            if self._pending_size > 0:
                cmds = b''.join(self._pending)
                self._pending, pending = [], self._pending
                self._pending_size, pending_size = 0, self._pending_size
                yield self.io.write(cmds)
        except tornado.iostream.StreamBufferFullError:
            self._pending = pending + self._pending
            self._pending_size += pending_size
        except tornado.iostream.StreamClosedError as e:
            self._pending = pending + self._pending
            self._pending_size += pending_size
            yield self._process_op_err(e)