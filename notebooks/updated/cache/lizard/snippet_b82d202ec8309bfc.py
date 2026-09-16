def get_user_identity(cls, instance_config):
    user = instance_config.get('user')
    if not (user and user.get('name') and user.get('password') and user.get
        ('domain') and user.get('domain').get('id')):
        raise IncompleteIdentity()
    identity = {'methods': ['password'], 'password': {'user': user}}
    return identity