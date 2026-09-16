def iterplayables():
    ls = DirScanner(stripdot=True)
    filt = lambda x: os.path.isdir(x) or x[-4:].lower() in ALLOWED_TYPES
    func = lambda x: '/'.join(x.split('/')[-2:])
    for x, y in ls.iteritems(want_files=True, want_dirs=False, func=func,
        filt=filt):
        yield {'name': x.decode('utf-8'), 'file_name': escape_utf8(y)}