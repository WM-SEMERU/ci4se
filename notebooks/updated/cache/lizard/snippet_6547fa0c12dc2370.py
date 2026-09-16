def get_body(self, environ=None):
    body = dict(status=self.code, message=self.description)
    errors = self.get_errors()
    if self.errors:
        body['errors'] = errors
    return json.dumps(body)