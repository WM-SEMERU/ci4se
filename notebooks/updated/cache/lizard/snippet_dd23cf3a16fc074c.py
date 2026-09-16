def expectRegion(self, filename, x, y, maxrms=0):
    log.debug('expectRegion %s (%s, %s)', filename, x, y)
    return self._expectFramebuffer(filename, x, y, maxrms)