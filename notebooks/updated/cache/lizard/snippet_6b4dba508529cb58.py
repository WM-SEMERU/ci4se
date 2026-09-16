def _wait_for_frame(self, timeout=None):
    frame = APIFrame(escaped=self._escaped)
    deadline = 0
    if timeout is not None and timeout > 0:
        deadline = time.time() + timeout
    while True:
        if self._callback and not self._thread_continue:
            raise ThreadQuitException
        if self.serial.inWaiting() == 0:
            if deadline and time.time() > deadline:
                raise _TimeoutException
            time.sleep(0.01)
            continue
        byte = self.serial.read()
        if byte != APIFrame.START_BYTE:
            continue
        if len(byte) == 1:
            frame.fill(byte)
        while frame.remaining_bytes() > 0:
            byte = self.serial.read()
            if len(byte) == 1:
                frame.fill(byte)
        try:
            frame.parse()
            if len(frame.data) == 0:
                frame = APIFrame()
                continue
            return frame
        except ValueError:
            frame = APIFrame(escaped=self._escaped)