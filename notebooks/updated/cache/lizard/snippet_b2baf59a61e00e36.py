def generateOneTimePad(self, userStore):
    pad = secureRandom(16).encode('hex')
    self._oneTimePads[pad] = userStore.idInParent

    def expirePad():
        self._oneTimePads.pop(pad, None)
    self.callLater(self.ONE_TIME_PAD_DURATION, expirePad)
    return pad