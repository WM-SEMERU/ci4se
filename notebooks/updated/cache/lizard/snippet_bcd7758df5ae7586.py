def _update(self, uri, body, **kwargs):
    self.run_hooks('modify_body_for_update', body, **kwargs)
    resp, resp_body = self.api.method_put(uri, body=body)
    return resp_body