def render_GET(self, request):
    request.setHeader(b'accept-ranges', b'bytes')
    producer = self.makeProducer(request, self.fileObject)
    if request.method == b'HEAD':
        return b''

    def done(ign):
        producer.stopProducing()
    request.notifyFinish().addCallbacks(done, done)
    producer.start()
    return server.NOT_DONE_YET