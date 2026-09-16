def abort(self):
    if self._smachine.state == State.CLOSED:
        return
    if self._smachine.state == State.READY:
        self._smachine.state = State.CLOSED
        return
    if self._smachine.state != State.CLOSING and self._transport.can_write_eof(
        ):
        self._transport.write_eof()
    self._close_transport()