def prepare_content_length(self, body):
    if body is not None:
        length = super_len(body)
        if length:
            self.headers['Content-Length'] = builtin_str(length)
    elif self.method not in ('GET', 'HEAD') and self.headers.get(
        'Content-Length') is None:
        self.headers['Content-Length'] = '0'