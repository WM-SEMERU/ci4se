def rec_load_all(self, zone):
    has_more = True
    current_count = 0
    while has_more:
        records = self._request({'a': 'rec_load_all', 'o': current_count,
            'z': zone})
        try:
            has_more = records['response']['recs']['has_more']
            current_count += records['response']['recs']['count']
            for record in records['response']['recs']['objs']:
                yield record
        except KeyError:
            has_more = False