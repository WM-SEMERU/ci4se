def send_response(self, code, message=None):
    self.log_request(code)
    self.send_response_only(code, message)
    self.send_header('Server', self.version_string())
    self.send_header('Date', self.date_time_string())