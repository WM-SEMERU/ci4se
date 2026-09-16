def emit(self, record):
    pickle = self.makePickle(record)
    connection = httplib.HTTPConnection(host=self.host, port=self.port,
        timeout=self.timeout)
    connection.request('POST', self.path, pickle, self.headers)