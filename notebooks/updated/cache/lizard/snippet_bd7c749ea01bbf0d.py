def concat(self, target, sources, **kwargs):
    if isinstance(sources, basestring):
        raise ValueError('sources should be a list')
    if any(',' in s for s in sources):
        raise NotImplementedError('WebHDFS does not support commas in concat')
    response = self._post(target, 'CONCAT', sources=','.join(sources), **kwargs
        )
    assert not response.content