def get_similar(self, limit=None):
    params = self._get_params()
    if limit:
        params['limit'] = limit
    doc = self._request(self.ws_prefix + '.getSimilar', True, params)
    names = _extract_all(doc, 'name')
    matches = _extract_all(doc, 'match')
    artists = []
    for i in range(0, len(names)):
        artists.append(SimilarItem(Artist(names[i], self.network), _number(
            matches[i])))
    return artists