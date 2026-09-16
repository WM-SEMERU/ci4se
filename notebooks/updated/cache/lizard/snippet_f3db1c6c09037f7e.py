def put_privileges(self, body, params=None):
    if body in SKIP_IN_PATH:
        raise ValueError("Empty value passed for a required argument 'body'.")
    return self.transport.perform_request('PUT', '/_security/privilege/',
        params=params, body=body)