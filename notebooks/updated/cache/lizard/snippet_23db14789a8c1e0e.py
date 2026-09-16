def check_public_ok(func):

    def wrapper(request, *args, **kwargs):
        default_to_open = getattr(settings, 'DEFAULT_TO_OPEN_READ', False)
        database_name = kwargs.get('database_name', '')
        collection_name = kwargs.get('collection_name', '')
        if not default_to_open:
            if not database_name or not collection_name:
                return HttpResponse(unauthorized_json_response(),
                    content_type='application/json')
            try:
                pub_read_api = PublicReadAPI.objects.get(database_name=
                    database_name, collection_name=collection_name)
            except PublicReadAPI.DoesNotExist:
                return HttpResponse(unauthorized_json_response(),
                    content_type='application/json')
            if pub_read_api.search_keys:
                search_key_list = shlex.split(pub_read_api.search_keys)
                keys = []
                for k in request.GET.keys():
                    if k not in search_key_list:
                        message = 'Search key %s is not allowed.' % k
                        body = {'code': 400, 'message': k, 'errors': [message]}
                        return HttpResponse(json.dumps(body, indent=4),
                            content_type='application/json')
        return func(request, *args, **kwargs)
    return update_wrapper(wrapper, func)