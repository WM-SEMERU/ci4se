def put_content(self, url, content):
    cache_path = self._url_to_path(url)
    try:
        dir = os.path.dirname(cache_path)
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise Error('Failed to create cache directories for ' % cache_path)
    try:
        with open(cache_path, 'wb') as f:
            f.write(content)
    except IOError:
        raise Error('Failed to cache content as %s for %s' % (cache_path, url))