def make_slack_blueprint(client_id=None, client_secret=None, scope=None,
    redirect_url=None, redirect_to=None, login_url=None, authorized_url=
    None, session_class=None, storage=None):
    scope = scope or ['identify', 'chat:write:bot']
    slack_bp = SlackBlueprint('slack', __name__, client_id=client_id,
        client_secret=client_secret, scope=scope, base_url=
        'https://slack.com/api/', authorization_url=
        'https://slack.com/oauth/authorize', token_url=
        'https://slack.com/api/oauth.access', redirect_url=redirect_url,
        redirect_to=redirect_to, login_url=login_url, authorized_url=
        authorized_url, session_class=session_class, storage=storage)
    slack_bp.from_config['client_id'] = 'SLACK_OAUTH_CLIENT_ID'
    slack_bp.from_config['client_secret'] = 'SLACK_OAUTH_CLIENT_SECRET'

    @slack_bp.before_app_request
    def set_applocal_session():
        ctx = stack.top
        ctx.slack_oauth = slack_bp.session
    return slack_bp