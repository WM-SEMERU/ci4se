def _handle_response(self, response):
    self.client.status = response.code
    self.response_headers = response.headers
    if self._method.upper() == 'HEAD' or response.code == NO_CONTENT:
        return succeed('')
    receiver = self.receiver_factory()
    receiver.finished = d = Deferred()
    receiver.content_length = response.length
    response.deliverBody(receiver)
    if response.code >= 400:
        d.addCallback(self._fail_response, response)
    return d