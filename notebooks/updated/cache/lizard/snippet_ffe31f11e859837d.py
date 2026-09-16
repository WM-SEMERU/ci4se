def http_basic(r, username, password):
    username = str(username)
    password = str(password)
    auth_s = b64encode('%s:%s' % (username, password))
    r.headers['Authorization'] = 'Basic %s' % auth_s
    return r