def build(cls, path):
    with zipfile.ZipFile(path) as zfile:
        items = ((name.replace('/', os.sep), zfile.getinfo(name)) for name in
            zfile.namelist())
        return dict(items)