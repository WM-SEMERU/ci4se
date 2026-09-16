def get_token(authed_user: hug.directives.user):
    user_model = Query()
    user = db.search(user_model.username == authed_user)[0]
    if user:
        out = {'user': user['username'], 'api_key': user['api_key']}
    else:
        out = {'error': 'User {0} does not exist'.format(authed_user)}
    return out