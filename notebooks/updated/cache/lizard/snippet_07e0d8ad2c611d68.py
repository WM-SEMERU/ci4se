def _password_digest(username, password):
    if not isinstance(password, basestring):
        raise TypeError('password must be an instance of basestring')
    if not isinstance(username, basestring):
        raise TypeError('username must be an instance of basestring')
    md5hash = hashlib.md5()
    md5hash.update('%s:mongo:%s' % (username.encode('utf-8'), password.
        encode('utf-8')))
    return unicode(md5hash.hexdigest())