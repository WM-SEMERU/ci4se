def stop(self, measurementId, failureReason=None):
    if failureReason is None:
        self.endResponseCode = self._doPut(self.sendURL + '/complete')
    else:
        self.endResponseCode = self._doPut(self.sendURL + '/failed', data={
            'failureReason': failureReason})
    self.sendURL = None