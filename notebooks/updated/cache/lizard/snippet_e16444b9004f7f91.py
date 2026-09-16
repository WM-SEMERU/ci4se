def metadefs_namespace_list(request, filters=None, sort_dir='asc', sort_key
    ='namespace', marker=None, paginate=False):
    if get_version() < 2:
        return [], False, False
    if filters is None:
        filters = {}
    limit = getattr(settings, 'API_RESULT_LIMIT', 1000)
    page_size = utils.get_page_size(request)
    if paginate:
        request_size = page_size + 1
    else:
        request_size = limit
    kwargs = {'filters': filters}
    if marker:
        kwargs['marker'] = marker
    kwargs['sort_dir'] = sort_dir
    kwargs['sort_key'] = sort_key
    namespaces_iter = glanceclient(request, '2').metadefs_namespace.list(
        page_size=request_size, limit=limit, **kwargs)
    resource_types = filters.get('resource_types')
    properties_target = filters.get('properties_target')
    if resource_types and properties_target:
        namespaces_iter = filter_properties_target(namespaces_iter,
            resource_types, properties_target)
    has_prev_data = False
    has_more_data = False
    if paginate:
        namespaces = list(itertools.islice(namespaces_iter, request_size))
        if len(namespaces) > page_size:
            namespaces.pop(-1)
            has_more_data = True
            if marker is not None:
                has_prev_data = True
        elif sort_dir == 'desc' and marker is not None:
            has_more_data = True
        elif marker is not None:
            has_prev_data = True
    else:
        namespaces = list(namespaces_iter)
    namespaces = [Namespace(namespace) for namespace in namespaces]
    return namespaces, has_more_data, has_prev_data