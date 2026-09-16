def _get_role_arn():
    role_arn = bottle.request.headers.get('X-Role-ARN')
    if not role_arn:
        role_arn = _lookup_ip_role_arn(bottle.request.environ.get(
            'REMOTE_ADDR'))
    if not role_arn:
        role_arn = _role_arn
    return role_arn