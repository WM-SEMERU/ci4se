def username_or(user, attr):
    if not settings.ACCOUNTS_NO_USERNAME:
        attr = 'username'
    value = getattr(user, attr)
    if callable(value):
        value = value()
    return value