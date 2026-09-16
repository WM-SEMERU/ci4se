def is_authenticated(user):
    if not hasattr(user, 'is_authenticated'):
        return False
    if callable(user.is_authenticated):
        return user.is_authenticated()
    else:
        return user.is_authenticated