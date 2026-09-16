def make_password(password, encoding='BCRYPT'):
    if encoding not in ['PLAIN', 'SSHA', 'BCRYPT']:
        raise ValueError('Unknown encoding %s' % encoding)
    if encoding == 'PLAIN':
        if isinstance(password, str) and six.PY2:
            password = six.text_type(password, 'utf-8')
        return '{PLAIN}%s' % password
    elif encoding == 'SSHA':
        salt = ''
        for n in range(7):
            salt += chr(randrange(256))
        salt = salt.encode('utf-8') if six.PY3 else salt
        if isinstance(password, six.text_type):
            password = password.encode('utf-8')
        else:
            password = str(password)
        b64_encoded = b64encode(hashlib.sha1(password + salt).digest() + salt)
        b64_encoded = b64_encoded.decode('utf-8') if six.PY3 else b64_encoded
        return '{SSHA}%s' % b64_encoded
    elif encoding == 'BCRYPT':
        password_hashed = bcrypt.hashpw(password.encode('utf-8') if
            isinstance(password, six.text_type) else password, bcrypt.gensalt()
            )
        if six.PY3:
            password_hashed = password_hashed.decode('utf-8')
        return '{BCRYPT}%s' % password_hashed