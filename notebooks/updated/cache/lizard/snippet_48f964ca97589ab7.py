def getAMFRequest(self, requests):
    envelope = remoting.Envelope(self.amf_version)
    if self.logger:
        self.logger.debug('AMF version: %s' % self.amf_version)
    for request in requests:
        service = request.service
        args = list(request.args)
        envelope[request.id] = remoting.Request(str(service), args)
    envelope.headers = self.headers
    return envelope