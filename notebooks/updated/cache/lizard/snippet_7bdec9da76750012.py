def failover(self, sync=None, force=None):
    req_body = self._cli.make_body(sync=sync, force=force)
    resp = self.action('failover', **req_body)
    resp.raise_if_err()
    return resp