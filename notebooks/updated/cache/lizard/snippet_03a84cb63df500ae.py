def cache_path_for_url(url):
    m = hashlib.md5()
    m.update(url)
    digest = m.hexdigest()
    return os.path.join(CACHE_DIRECTORY, '%s.html' % digest)