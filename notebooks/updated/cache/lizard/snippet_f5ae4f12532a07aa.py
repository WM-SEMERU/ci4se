def setup_request_sessions(self):
    self.req_session = requests.Session()
    self.req_session.headers.update(self.headers)