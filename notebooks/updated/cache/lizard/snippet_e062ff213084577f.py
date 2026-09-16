def OPTIONS_preflight(self, path_info):
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE')
    self.send_header('Access-Control-Allow-Headers',
        'content-type, authorization, range')
    self.send_header('Access-Control-Expose-Headers',
        'content-length, content-range')
    self.send_header('Access-Control-Max-Age', 21600)
    self.end_headers()
    return