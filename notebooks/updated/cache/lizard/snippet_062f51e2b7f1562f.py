def load(self, response):
    self._response = response
    if self.next_location(raw=True):
        self._num_redirects += 1