def _recv_frameify(self, data):
    state = self._recv_framer_state
    framer = None
    frameify = None
    while True:
        if framer != self._recv_framer:
            if frameify:
                try:
                    frameify.throw(framers.FrameSwitch)
                except StopIteration:
                    pass
            framer = self._recv_framer
            state._reset(framer)
            frameify = framer.frameify(state, data)
            data = ''
        try:
            frame = frameify.next()
        except StopIteration:
            break
        if self._application:
            self._application.recv_frame(frame)