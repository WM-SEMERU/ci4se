def login(provider_id):
    provider = get_provider_or_404(provider_id)
    callback_url = get_authorize_callback('login', provider_id)
    post_login = request.form.get('next', get_post_login_redirect())
    session[config_value('POST_OAUTH_LOGIN_SESSION_KEY')] = post_login
    return provider.authorize(callback_url)