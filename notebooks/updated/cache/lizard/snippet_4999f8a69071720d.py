def disconnect(self, receipt=None, headers=None, **keyword_headers):
    Protocol11.disconnect(self, receipt, headers, **keyword_headers)
    self.transport.stop()