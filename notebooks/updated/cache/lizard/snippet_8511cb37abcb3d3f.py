def key_gen(self, key_name, type, size=2048, **kwargs):
    opts = {'type': type, 'size': size}
    kwargs.setdefault('opts', opts)
    args = key_name,
    return self._client.request('/key/gen', args, decoder='json', **kwargs)