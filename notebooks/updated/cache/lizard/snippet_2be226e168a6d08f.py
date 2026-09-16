def do_HEAD(self):
    self.queue.put(self.headers.get('User-Agent'))
    self.send_response(six.moves.BaseHTTPServer.HTTPStatus.OK)
    self.send_header('Location', self.path)
    self.end_headers()