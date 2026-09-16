def get(self, timeout=None, block=True, throw_dead=True):
    _vv and IOLOG.debug('%r.get(timeout=%r, block=%r)', self, timeout, block)
    try:
        msg = self._latch.get(timeout=timeout, block=block)
    except LatchError:
        raise ChannelError(self.closed_msg)
    if msg.is_dead and throw_dead:
        msg._throw_dead()
    return msg