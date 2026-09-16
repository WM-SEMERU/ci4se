def handle_POST(self):
    self.send_response(404)
    self.end_headers()
    self.wfile.write('not found'.encode('utf8'))