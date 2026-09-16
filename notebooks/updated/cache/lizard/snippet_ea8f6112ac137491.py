def inject(self, contents=None, **kwargs):
    if contents and not isinstance(contents, dict):
        raise WrongContentError(self, contents, 'contents should be a dict')
    self._stable = False
    if not contents:
        contents = {}
    if kwargs:
        contents.update(kwargs)
    self.content_data.update(contents)
    return self