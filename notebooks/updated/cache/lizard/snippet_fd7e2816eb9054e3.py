def msearch_template(self, body, index=None, params=None):
    if body in SKIP_IN_PATH:
        raise ValueError("Empty value passed for a required argument 'body'.")
    return self.transport.perform_request('GET', _make_path(index,
        '_msearch', 'template'), params=params, body=self._bulk_body(body),
        headers={'content-type': 'application/x-ndjson'})