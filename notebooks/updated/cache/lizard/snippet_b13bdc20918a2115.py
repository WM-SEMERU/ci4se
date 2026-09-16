def mkdir_p(dir):
    if not dir:
        return
    if dir.endswith('/') or dir.endswith('\\'):
        mkdir_p(dir[:-1])
        return
    if os.path.isdir(dir):
        return
    mkdir_p(os.path.dirname(dir))
    try:
        os.mkdir(dir)
    except Exception:
        pass