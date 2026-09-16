def oauth_logout_handler(sender_app, user=None):
    oauth = current_app.extensions['oauthlib.client']
    for remote in oauth.remote_apps.values():
        token_delete(remote)
    db.session.commit()