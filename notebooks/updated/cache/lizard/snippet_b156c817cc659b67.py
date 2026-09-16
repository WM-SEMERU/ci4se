def require_content_type(self, content_type):
    if self.request.headers.get('content-type', '') != content_type:
        self.halt(400, 'Content type must be ' + content_type)