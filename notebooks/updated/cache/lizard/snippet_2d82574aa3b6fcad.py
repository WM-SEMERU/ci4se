def _parse_mirteFile(path, logger=None):
    l = logging.getLogger('_parse_mirteFile') if logger is None else logger
    cache_path = os.path.join(os.path.dirname(path), 
        CACHE_FILENAME_TEMPLATE % os.path.basename(path))
    if os.path.exists(cache_path) and os.path.getmtime(cache_path
        ) >= os.path.getmtime(path):
        with open(cache_path) as f:
            return msgpack.unpack(f)
    with open(path) as f:
        ret = yaml.load(f)
    try:
        with open(cache_path, 'w') as f:
            msgpack.pack(ret, f)
    except IOError as e:
        if e.errno == errno.EACCES:
            l.warn('Not allowed to write %s', path)
        else:
            raise
    return ret