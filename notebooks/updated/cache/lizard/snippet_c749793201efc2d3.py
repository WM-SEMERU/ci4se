def until_state(self, state, timeout=None):
    if state not in self._valid_states:
        raise ValueError('State must be one of {0}, not {1}'.format(self.
            _valid_states, state))
    if state != self._state:
        if timeout:
            return with_timeout(self._ioloop.time() + timeout, self.
                _waiting_futures[state], self._ioloop)
        else:
            return self._waiting_futures[state]
    else:
        f = tornado_Future()
        f.set_result(True)
        return f