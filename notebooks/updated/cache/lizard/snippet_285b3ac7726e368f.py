def list(self, request, *args, **kwargs):
    search_kwargs = {'published': False}
    query_params = get_query_params(self.request)
    for field_name in 'status':
        if field_name in query_params:
            search_kwargs[field_name] = query_params.get(field_name)
    if 'search' in query_params:
        search_kwargs['query'] = query_params.get('search')
    if 'active' in query_params:
        del search_kwargs['published']
        search_kwargs['active'] = True
    if 'closed' in query_params:
        del search_kwargs['published']
        search_kwargs['closed'] = True
    queryset = self.model.search_objects.search(**search_kwargs)
    page = self.paginate_queryset(queryset)
    if page is not None:
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)