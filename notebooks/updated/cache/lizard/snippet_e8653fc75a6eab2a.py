def split_path_and_file(s):
    _path = s
    _filename = ''
    try:
        x = os.path.split(s)
        _path = x[0]
        _filename = x[1]
    except Exception:
        print('Error: unable to split path')
    return _path, _filename