def update(self, index, id, doc_type='_doc', body=None, params=None):
    for param in (index, id):
        if param in SKIP_IN_PATH:
            raise ValueError('Empty value passed for a required argument.')
    return self.transport.perform_request('POST', _make_path(index,
        doc_type, id, '_update'), params=params, body=body)