def gen_etag():
    my_salt = gen_uuid()
    if six.PY2:
        my_salt = my_salt.decode('utf-8')
    elif six.PY3:
        my_salt = my_salt.encode('utf-8')
    md5 = hashlib.md5()
    md5.update(my_salt)
    return md5.hexdigest()