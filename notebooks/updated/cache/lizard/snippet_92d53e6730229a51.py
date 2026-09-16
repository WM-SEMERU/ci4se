def handle_json_wrapper_GET(self, handler, parsed_params):
    schedule = self.server.schedule
    result = handler(parsed_params)
    content = ResultEncoder().encode(result)
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', str(len(content)))
    self.end_headers()
    self.wfile.write(content)