def write_error(self, status_code, **kwargs):
    reason = self._reason
    if self.settings.get('serve_traceback') and 'exc_info' in kwargs:
        error = []
        for line in traceback.format_exception(*kwargs['exc_info']):
            error.append(line)
    else:
        error = None
    data = {'_traceback': error, 'message': reason, 'code': status_code}
    content = self.render_exception(**data)
    self.write(content)