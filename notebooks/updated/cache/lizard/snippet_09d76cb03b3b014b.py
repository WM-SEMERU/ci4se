def init(req, model):
    limit = req.get_param('page[limit]') or goldman.config.PAGE_LIMIT
    offset = req.get_param('page[offset]') or 0
    try:
        return Paginator(limit, offset)
    except ValueError:
        raise InvalidQueryParams(**{'detail':
            "The page['limit'] & page['offset'] query params may only be specified once each & must both be an integer >= 0."
            , 'links': 'jsonapi.org/format/#fetching-pagination',
            'parameter': 'page'})