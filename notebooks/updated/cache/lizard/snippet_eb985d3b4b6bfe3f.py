def _path_hash(path, transform, kwargs):
    sortedargs = [('%s:%r:%s' % (key, value, type(value))) for key, value in
        sorted(iteritems(kwargs))]
    srcinfo = '{path}:{transform}:{{{kwargs}}}'.format(path=os.path.abspath
        (path), transform=transform, kwargs=','.join(sortedargs))
    return digest_string(srcinfo)