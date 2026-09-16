def getPos(self, text):
    kwargs = {'text': text}
    kwargs = {k: (dumps(v) if type(v) is dict else v) for k, v in kwargs.
        items()}
    param_rest = self._make_rest('text', **kwargs)
    url = self._basePath + '/lexical/pos'.format(**kwargs)
    requests_params = {k: v for k, v in kwargs.items() if k != 'text'}
    return self._get('GET', url, requests_params)