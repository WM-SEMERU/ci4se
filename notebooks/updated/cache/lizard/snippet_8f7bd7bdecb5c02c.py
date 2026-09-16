def artist_update(self, artist_id, name=None, urls=None, alias=None, group=None
    ):
    params = {'id': artist_id, 'artist[name]': name, 'artist[urls]': urls,
        'artist[alias]': alias, 'artist[group]': group}
    return self._get('artist/update', params, method='PUT')