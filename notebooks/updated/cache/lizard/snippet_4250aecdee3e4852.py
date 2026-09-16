def vehicles(self, vid=None, rt=None):
    if vid and rt:
        raise ValueError(
            'The `vid` and `route` parameters cannot be specified simultaneously.'
            )
    if not (vid or rt):
        raise ValueError('You must specify either the `vid` or `rt` parameter.'
            )
    if listlike(rt):
        rt = ','.join(map(str, rt))
    if listlike(vid):
        vid = ','.join(map(str, vid))
    url = self.endpoint('VEHICLES', dict(vid=vid, rt=rt))
    return self.response(url)