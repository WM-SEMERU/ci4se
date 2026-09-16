def md5_string(s):
    m = hashlib.md5()
    m.update(s)
    return str(m.hexdigest())