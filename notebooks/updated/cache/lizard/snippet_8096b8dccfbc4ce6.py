def verifyWriteMode(files):
    if not isinstance(files, list):
        files = [files]
    not_writable = []
    writable = True
    for fname in files:
        try:
            f = open(fname, 'a')
            f.close()
            del f
        except:
            not_writable.append(fname)
            writable = False
    if not writable:
        print('The following file(s) do not have write permission!')
        for fname in not_writable:
            print('    ', fname)
    return writable