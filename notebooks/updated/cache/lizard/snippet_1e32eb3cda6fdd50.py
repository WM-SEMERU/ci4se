def deactivate_users(server_context, target_ids, container_path=None):
    response = __make_user_api_request(server_context, target_ids=
        target_ids, api='deactivateUsers.view', container_path=container_path)
    if response is not None and response['status_code'] == 200:
        return dict(success=True)
    else:
        raise ValueError('Unable to deactivate users {0}'.format(target_ids))