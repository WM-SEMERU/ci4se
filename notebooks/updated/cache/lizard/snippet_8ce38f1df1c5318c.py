def delete_user(username, token_manager=None, app_url=defaults.APP_URL):
    account_id = get_account_id(username, token_manager=token_manager,
        app_url=app_url)
    headers = token_manager.get_access_token_headers()
    auth_url = environment.get_auth_url(app_url=app_url)
    url = '%s/api/v1/accounts/%s' % (auth_url, account_id)
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        return response.text
    else:
        raise JutException('Error %s; %s' % (response.status_code, response
            .text))