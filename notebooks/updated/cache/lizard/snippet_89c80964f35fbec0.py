def list(self, offset=0, limit=0, fields=None, sort=None, **kwargs):
    try:
        cursor = self._cursor(offset=offset, limit=limit, fields=fields,
            sort=sort, **kwargs)
        return list(cursor), cursor.count()
    except pymongo.errors.OperationFailure as exc:
        try:
            kwargs['$or'][0]['$text']['$search']
        except (KeyError, IndexError):
            raise exc
        LOG.warn('Falling back to hard-coded mongo v2.4 search behavior')
        kwargs = self.search_alternative(limit, **kwargs)
        LOG.debug('Modified kwargs: %s', kwargs)
        cursor = self._cursor(offset=offset, limit=limit, fields=fields,
            sort=sort, **kwargs)
        return list(cursor), cursor.count()