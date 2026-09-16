def md5sum(string):
    h = hashlib.new('md5')
    h.update(string.encode('utf-8'))
    return h.hexdigest()