def recompile(filename):
    import os
    import imp
    import marshal
    import struct
    f = open(filename, 'U')
    try:
        timestamp = long(os.fstat(f.fileno()).st_mtime)
    except AttributeError:
        timestamp = long(os.stat(filename).st_mtime)
    codestring = f.read()
    f.close()
    if codestring and codestring[-1] != '\n':
        codestring = codestring + '\n'
    try:
        codeobject = compile(codestring, filename, 'exec')
    except SyntaxError:
        print >> sys.stderr, 'Skipping %s - syntax error.' % filename
        return
    cod = Code.from_code(codeobject)
    message = 'reassembled %r imported.\n' % filename
    cod.code[:0] = [(LOAD_GLOBAL, '__import__'), (LOAD_CONST, 'sys'), (
        CALL_FUNCTION, 1), (LOAD_ATTR, 'stderr'), (LOAD_ATTR, 'write'), (
        LOAD_CONST, message), (CALL_FUNCTION, 1), (POP_TOP, None)]
    codeobject2 = cod.to_code()
    fc = open(filename + 'c', 'wb')
    fc.write('\x00\x00\x00\x00')
    fc.write(struct.pack('<l', timestamp))
    marshal.dump(codeobject2, fc)
    fc.flush()
    fc.seek(0, 0)
    fc.write(imp.get_magic())
    fc.close()