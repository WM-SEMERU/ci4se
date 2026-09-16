def next(self):
    if self._stopped_iteration:
        raise StopIteration()
    while True:
        try:
            chunk = self.process._pipe_queue.get(True, 0.001)
        except Empty:
            if self.call_args['iter_noblock']:
                return errno.EWOULDBLOCK
        else:
            if chunk is None:
                self.wait()
                self._stopped_iteration = True
                raise StopIteration()
            try:
                return chunk.decode(self.call_args['encoding'], self.
                    call_args['decode_errors'])
            except UnicodeDecodeError:
                return chunk