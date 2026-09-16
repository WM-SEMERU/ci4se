def _sendBuffers(self):
    msg = {}
    msg_size = 0
    lastlog = None
    logdata = []
    while self.buffered:
        logname, data = self.buffered.popleft()
        if lastlog is None:
            lastlog = logname
        elif logname != lastlog:
            self._sendMessage(msg)
            msg = {}
            msg_size = 0
        lastlog = logname
        logdata = msg.setdefault(logname, [])
        for chunk in self._chunkForSend(data):
            if not chunk:
                continue
            logdata.append(chunk)
            msg_size += len(chunk)
            if msg_size >= self.CHUNK_LIMIT:
                self._sendMessage(msg)
                msg = {}
                logdata = msg.setdefault(logname, [])
                msg_size = 0
    self.buflen = 0
    if logdata:
        self._sendMessage(msg)
    if self.sendBuffersTimer:
        if self.sendBuffersTimer.active():
            self.sendBuffersTimer.cancel()
        self.sendBuffersTimer = None