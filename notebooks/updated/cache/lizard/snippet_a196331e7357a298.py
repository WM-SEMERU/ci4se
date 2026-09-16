async def patch_entries(self, entry, **kwargs):
    params = {'access_token': self.token, 'title': '', 'tags': []}
    if 'title' in kwargs:
        params['title'] = kwargs['title']
    if 'tags' in kwargs and isinstance(kwargs['tags'], list):
        params['tags'] = ', '.join(kwargs['tags'])
    params['archive'] = self.__get_attr(what='archive', type_attr=int,
        value_attr=(0, 1), **kwargs)
    params['starred'] = self.__get_attr(what='starred', type_attr=int,
        value_attr=(0, 1), **kwargs)
    params['order'] = self.__get_attr(what='order', type_attr=str,
        value_attr=('asc', 'desc'), **kwargs)
    path = '/api/entries/{entry}.{ext}'.format(entry=entry, ext=self.format)
    return await self.query(path, 'patch', **params)