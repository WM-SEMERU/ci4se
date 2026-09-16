def rm(self, path, cycle=';*'):
    rdir = self
    with preserve_current_directory():
        dirname, objname = os.path.split(os.path.normpath(path))
        if dirname:
            rdir = rdir.Get(dirname)
        rdir.Delete(objname + cycle)