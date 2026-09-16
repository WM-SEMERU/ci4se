def read_files(path, verbose=True):
    for filehandle in filehandles(path, verbose=verbose):
        yield CTfile.load(filehandle)