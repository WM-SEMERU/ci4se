def login(token, apikey, username, password):
    if manual_login_success(token, username, password):
        return
    if not apikey:
        if has_browser():
            apikey = wait_for_apikey()
        else:
            floyd_logger.error(
                'No browser found, please login manually by creating login key at %s/settings/apikey.'
                , floyd.floyd_web_host)
            sys.exit(1)
    if apikey:
        user = AuthClient().get_user(apikey, is_apikey=True)
        AuthConfigManager.set_apikey(username=user.username, apikey=apikey)
        floyd_logger.info('Login Successful as %s', user.username)
    else:
        floyd_logger.error(
            'Login failed, please see --help for other login options.')