def _get_paging_controls(request):
    start = request.url.query.get('start', None)
    limit = request.url.query.get('limit', None)
    controls = {}
    if limit is not None:
        try:
            controls['limit'] = int(limit)
        except ValueError:
            LOGGER.debug('Request query had an invalid limit: %s', limit)
            raise errors.CountInvalid()
        if controls['limit'] <= 0:
            LOGGER.debug('Request query had an invalid limit: %s', limit)
            raise errors.CountInvalid()
    if start is not None:
        controls['start'] = start
    return controls