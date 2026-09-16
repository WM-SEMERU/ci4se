def generate_secured_key(value, key_nonce_separator='.', nonce_length=4,
    base=BASE62):
    if not isinstance(value, (int, long)):
        raise ValueError()
    posix_time = int(time.mktime(datetime.datetime.now().timetuple()))
    nonce = hashlib.md5(str(posix_time)).hexdigest()[:nonce_length]
    key = int_to_key(value, base=base)
    return key, nonce, '%s%s%s' % (key, key_nonce_separator, nonce)