def get(self, **kwargs):
    default_results_size = current_app.config.get(
        'RECORDS_REST_DEFAULT_RESULTS_SIZE', 10)
    page = request.values.get('page', 1, type=int)
    size = request.values.get('size', default_results_size, type=int)
    if page * size >= self.max_result_window:
        raise MaxResultWindowRESTError()
    urlkwargs = dict()
    search_obj = self.search_class()
    search = search_obj.with_preference_param().params(version=True)
    search = search[(page - 1) * size:page * size]
    search, qs_kwargs = self.search_factory(search)
    urlkwargs.update(qs_kwargs)
    search_result = search.execute()
    urlkwargs.update(size=size, _external=True)
    endpoint = '.{0}_list'.format(current_records_rest.
        default_endpoint_prefixes[self.pid_type])
    links = dict(self=url_for(endpoint, page=page, **urlkwargs))
    if page > 1:
        links['prev'] = url_for(endpoint, page=page - 1, **urlkwargs)
    if (size * page < search_result.hits.total and size * page < self.
        max_result_window):
        links['next'] = url_for(endpoint, page=page + 1, **urlkwargs)
    return self.make_response(pid_fetcher=self.pid_fetcher, search_result=
        search_result.to_dict(), links=links, item_links_factory=self.
        item_links_factory)