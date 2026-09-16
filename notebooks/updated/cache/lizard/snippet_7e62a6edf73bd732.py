def find_module(self, fullname, path=None):
    basepaths = [''] + list(sys.path)
    if fullname.startswith('.'):
        if path is None:
            return None
        fullname = fullname[1:]
        basepaths.insert(0, path)
    fullpath = os.path.join(*fullname.split('.'))
    for head in basepaths:
        path = os.path.join(head, fullpath)
        filepath = path + self.ext
        dirpath = os.path.join(path, '__init__' + self.ext)
        if os.path.exists(filepath):
            self.run_compiler(filepath)
            return None
        if os.path.exists(dirpath):
            self.run_compiler(path)
            return None
    return None