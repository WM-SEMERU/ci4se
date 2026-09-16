def _get_codename(self, pathname, basename):
    file_py = pathname + '.py'
    file_pyc = pathname + '.pyc'
    file_pyo = pathname + '.pyo'
    if os.path.isfile(file_pyo) and os.stat(file_pyo).st_mtime >= os.stat(
        file_py).st_mtime:
        fname = file_pyo
    elif not os.path.isfile(file_pyc) or os.stat(file_pyc).st_mtime < os.stat(
        file_py).st_mtime:
        import py_compile
        if self.debug:
            print('Compiling', file_py)
        try:
            py_compile.compile(file_py, file_pyc, None, True)
        except py_compile.PyCompileError as err:
            print(err.msg)
        fname = file_pyc
    else:
        fname = file_pyc
    archivename = os.path.split(fname)[1]
    if basename:
        archivename = '%s/%s' % (basename, archivename)
    return fname, archivename