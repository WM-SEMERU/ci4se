def open(self):
    sess_id = self._get_sess_id()
    if sess_id:
        self.application.pc.websockets[self._get_sess_id()] = self
        self.write_message(json.dumps({'cmd': 'status', 'status': 'open'}))
    else:
        self.write_message(json.dumps({'cmd': 'error', 'error':
            'Please login', 'code': 401}))