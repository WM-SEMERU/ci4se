def _build_keys(self, slug, date=None, granularity='all'):
    slug = slugify(slug)
    if date is None:
        date = datetime.utcnow()
    patts = self._build_key_patterns(slug, date)
    if granularity == 'all':
        return list(patts.values())
    return [patts[granularity]]