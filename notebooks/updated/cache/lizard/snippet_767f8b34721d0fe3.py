def get(self, *args, **kwargs):
    if 'convert' in kwargs:
        conversion = kwargs.pop('convert')
    else:
        conversion = True
    kwargs = self._get_keywords(**kwargs)
    url = self._create_path(*args)
    request = self.session.get(url, params=kwargs)
    content = request.content
    self._request = request
    return self.convert(content, conversion)