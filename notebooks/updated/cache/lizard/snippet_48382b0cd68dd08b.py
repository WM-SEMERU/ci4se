def __make_security_group_api_request(server_context, api, user_ids,
    group_id, container_path):
    url = server_context.build_url(security_controller, api, container_path)
    if not hasattr(user_ids, '__iter__'):
        user_ids = [user_ids]
    return server_context.make_request(url, {'groupId': group_id,
        'principalIds': user_ids})