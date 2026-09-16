def _push_from_buffer(self):
    if len(self.buffer) > 0:
        if time.time() - self.last_sent_time > 5:
            try:
                message = self.buffer.pop(0)
                self.s.send(message.encode('utf-8'))
                if self.verbose:
                    print(message)
            finally:
                self.last_sent_time = time.time()