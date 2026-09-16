def status(self, indices=None):
    path = self.conn._make_path(indices, (), '_status', allow_all_indices=False
        )
    return self.conn._send_request('GET', path)