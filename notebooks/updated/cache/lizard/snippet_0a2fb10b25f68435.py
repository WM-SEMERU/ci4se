def request(self, method, *parts, **options):
    if len(parts) != 0:
        return self.__call__(*parts).request(method=method, **options)
    else:
        if 'url' not in options:
            options['url'] = self.url()
        for key, value in six.iteritems(self.config):
            if value is not None:
                if isinstance(value, dict):
                    copy = value.copy()
                    if options.get(key):
                        copy.update(options[key])
                    options[key] = copy
                else:
                    options.setdefault(key, value)
        return self._parent.request(method=method, **options)