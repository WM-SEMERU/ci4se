def browse_userjournals(self, username, featured=False, offset=0, limit=10):
    response = self._req('/browse/user/journals', {'username': username,
        'featured': featured, 'offset': offset, 'limit': limit})
    deviations = []
    for item in response['results']:
        d = Deviation()
        d.from_dict(item)
        deviations.append(d)
    return {'results': deviations, 'has_more': response['has_more'],
        'next_offset': response['next_offset']}