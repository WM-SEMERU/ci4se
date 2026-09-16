def push(self, request):
    self.server.lpush(self.key, self._encode_request(request))