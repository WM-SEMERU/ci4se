def _user(self, user, real_name):
    with self.lock:
        self.send('USER %s 0 * :%s' % (user, real_name))
        if self.readable():
            self._recv()
            self.stepback()