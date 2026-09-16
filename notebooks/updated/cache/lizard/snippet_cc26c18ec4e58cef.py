def calculate_nonce(timestamp, secret, salt=None):
    if not salt:
        salt = ''.join([random.choice('0123456789ABCDEF') for x in range(4)])
    return '%s:%s:%s' % (timestamp, salt, md5.md5('%s:%s:%s' % (timestamp,
        salt, secret)).hexdigest())