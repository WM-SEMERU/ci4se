def ProgramScanner(**kw):
    kw['path_function'] = SCons.Scanner.FindPathDirs('LIBPATH')
    ps = SCons.Scanner.Base(scan, 'ProgramScanner', **kw)
    return ps