def __setLock(self, command):
    if command in (TURN_ON, TURN_OFF):
        self._operation = command
    elif command in INV_SOURCES:
        self._operation = SOURCE
    else:
        self._operation = ALL
    self._isLocked = True
    self._timer = time.time()