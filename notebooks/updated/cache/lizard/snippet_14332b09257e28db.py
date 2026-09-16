def get_settings(self, index=None):
    path = make_path(index, '_settings')
    return self.conn._send_request('GET', path)