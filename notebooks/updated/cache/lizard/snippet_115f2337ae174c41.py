def with_body(self, body):
    try:
        self.body = body.encode('utf-8')
    except:
        try:
            self.body = bytes(body)
        except:
            raise ValueError(
                'Request body must be a string or bytes-like object.')
    hasher = hashlib.sha256()
    hasher.update(self.body)
    digest = base64.b64encode(hasher.digest()).decode('utf-8')
    self.with_header('X-Authorization-Content-Sha256', digest)
    return self