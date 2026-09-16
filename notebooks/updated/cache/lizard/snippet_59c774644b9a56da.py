def appname(path=None):
    if path is None:
        path = sys.argv[0]
    name = os.path.basename(os.path.splitext(path)[0])
    if name == 'mod_wsgi':
        name = 'nvn_web'
    return name