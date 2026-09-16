def plugins(self, plugin_type='all', sort='id', direction='asc', size=1000,
    offset=0, all=True, loops=0, since=None, **filterset):
    plugins = []
    payload = {'size': size, 'offset': offset, 'type': plugin_type,
        'sortField': sort, 'sortDirection': direction.upper()}
    if len(filterset) > 0:
        fname = list(filterset.keys())[0]
        if fname in self._xrefs:
            fname = 'xrefs:%s' % fname.replace('_', '-')
        payload['filterField'] = fname
        payload['filterString'] = filterset[list(filterset.keys())[0]]
    if since is not None and isinstance(since, date):
        payload['since'] = calendar.timegm(since.utctimetuple())
    while all or loops > 0:
        data = self.raw_query('plugin', 'init', data=payload)
        if not data:
            return []
        for plugin in data['plugins']:
            plugins.append(plugin)
        if len(data['plugins']) < size:
            all = False
            loops = 0
        else:
            loops -= 1
            payload['offset'] += len(data['plugins'])
    return plugins