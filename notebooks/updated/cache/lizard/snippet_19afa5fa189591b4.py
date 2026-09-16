def get_home():
    path = ''
    try:
        path = os.path.expanduser('~')
    except:
        pass
    if not os.path.isdir(path):
        for evar in ('HOME', 'USERPROFILE', 'TMP'):
            try:
                path = os.environ[evar]
                if os.path.isdir(path):
                    break
            except:
                pass
    if path:
        return path
    else:
        raise RuntimeError('please define environment variable $HOME')