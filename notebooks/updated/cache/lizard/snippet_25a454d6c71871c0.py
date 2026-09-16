def render_POST(self, request):
    from twisted.internet.defer import maybeDeferred
    chain = self.factory.newInstance()
    data = request.content.read()
    d = maybeDeferred(chain.processRequest, data, request=request, resource
        =self)
    d.addCallback(chain.processResponse, request=request, resource=self)
    d.addCallback(self._writeResponse, request)
    d.addErrback(self._writeFault, request)
    return NOT_DONE_YET