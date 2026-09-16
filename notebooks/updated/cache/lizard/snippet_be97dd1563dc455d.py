def login_handler(response, provider, query):
    connection = _datastore.find_connection(**query)
    if connection:
        after_this_request(_commit)
        token_pair = get_token_pair_from_oauth_response(provider, response)
        if token_pair['access_token'] != connection.access_token or token_pair[
            'secret'] != connection.secret:
            connection.access_token = token_pair['access_token']
            connection.secret = token_pair['secret']
            _datastore.put(connection)
        user = connection.user
        login_user(user)
        key = _social.post_oauth_login_session_key
        redirect_url = session.pop(key, get_post_login_redirect())
        login_completed.send(current_app._get_current_object(), provider=
            provider, user=user)
        return redirect(redirect_url)
    login_failed.send(current_app._get_current_object(), provider=provider,
        oauth_response=response)
    next = get_url(_security.login_manager.login_view)
    msg = '%s account not associated with an existing user' % provider.name
    do_flash(msg, 'error')
    return redirect(next)