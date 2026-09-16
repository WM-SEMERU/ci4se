def fixMissingPythonLib(self, binaries):
    if is_aix:
        names = 'libpython%d.%d.a' % sys.version_info[:2],
    elif is_unix:
        names = 'libpython%d.%d.so' % sys.version_info[:2],
    elif is_darwin:
        names = 'Python', 'libpython%d.%d.dylib' % sys.version_info[:2]
    else:
        return
    for nm, fnm, typ in binaries:
        for name in names:
            if typ == 'BINARY' and name in fnm:
                return
    name = names[0]
    if is_unix:
        lib = bindepend.findLibrary(name)
        if lib is None:
            raise IOError('Python library not found!')
    elif is_darwin:
        lib = os.path.join(sys.exec_prefix, 'Python')
        if not os.path.exists(lib):
            raise IOError('Python library not found!')
    binaries.append((os.path.split(lib)[1], lib, 'BINARY'))