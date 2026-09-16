def add_version(self, name, url, mimetype=None, on_duplicate='error', **kwargs
    ):
    if not mimetype:
        raise ValueError('mimetype parameter to add_version is required')
    if on_duplicate != 'ignore':
        if url in self._seen_versions:
            if on_duplicate == 'error':
                raise ValueError('duplicate version url %s' % url)
            elif on_duplicate == 'use_new':
                self['versions'] = [v for v in self['versions'] if v['url'] !=
                    url]
            elif on_duplicate == 'use_old':
                return
        self._seen_versions.add(url)
    d = dict(name=name, url=url, mimetype=mimetype, **kwargs)
    self['versions'].append(d)