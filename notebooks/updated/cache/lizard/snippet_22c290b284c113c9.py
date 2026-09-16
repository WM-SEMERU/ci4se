def values(self, **kwargs):
    result = yield self.get(**kwargs)
    if not result['rows']:
        raise Return([])
    raise Return([x['value'] for x in result['rows']])