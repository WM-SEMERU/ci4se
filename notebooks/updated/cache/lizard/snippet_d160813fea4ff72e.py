def Proxy(self, status, headers, exc_info=None):
    self.call_context['status'] = status
    self.call_context['headers'] = headers
    self.call_context['exc_info'] = exc_info
    return self.body_buffer.write