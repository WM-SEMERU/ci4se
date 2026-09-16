def sendFragmentStart(self, data):
    opcode = BINARY
    if _check_unicode(data):
        opcode = TEXT
    self._sendMessage(True, opcode, data)