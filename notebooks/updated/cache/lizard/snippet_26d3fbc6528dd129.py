def waitUpTo(self, timeoutSeconds, pollInterval=DEFAULT_POLL_INTERVAL):
    i = 0
    numWaits = timeoutSeconds / float(pollInterval)
    ret = self.poll()
    if ret is None:
        while i < numWaits:
            time.sleep(pollInterval)
            ret = self.poll()
            if ret is not None:
                break
            i += 1
    return ret