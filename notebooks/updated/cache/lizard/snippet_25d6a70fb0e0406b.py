def fingerprints(data):
    Hashes = namedtuple('Hashes', 'md5 sha1 sha256 sha512')
    if six.PY2:
        if not isinstance(data, str):
            data = data.encode('utf-8')
    elif six.PY3:
        if not isinstance(data, bytes):
            data = data.encode('utf-8')
    md5 = hashlib.md5()
    md5.update(data)
    md5 = md5.hexdigest()
    sha1 = hashlib.sha1()
    sha1.update(data)
    sha1 = sha1.hexdigest()
    sha256 = hashlib.sha256()
    sha256.update(data)
    sha256 = sha256.hexdigest()
    sha512 = hashlib.sha512()
    sha512.update(data)
    sha512 = sha512.hexdigest()
    return Hashes(md5, sha1, sha256, sha512)