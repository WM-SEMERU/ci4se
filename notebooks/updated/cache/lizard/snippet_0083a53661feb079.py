def find_file_structure(self, body, params=None):
    if body in SKIP_IN_PATH:
        raise ValueError("Empty value passed for a required argument 'body'.")
    return self.transport.perform_request('POST',
        '/_ml/find_file_structure', params=params, body=self._bulk_body(body))