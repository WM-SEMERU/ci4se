def isRunning(self, waitTime=0):
    waitUntil = time.time() + waitTime
    while True:
        if self.getPID() > 0:
            return True
        else:
            self._pid = PlatformManager.getWindowPID(PlatformManager.
                getWindowByTitle(re.escape(self._title)))
        if time.time() > waitUntil:
            break
        else:
            time.sleep(self._defaultScanRate)
    return self.getPID() > 0