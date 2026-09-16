def set_user_password(environment, parameter, password):
    username = '%s:%s' % (environment, parameter)
    return password_set(username, password)