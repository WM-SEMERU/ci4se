def logger(filter='WARN'):
    import os, shutil, tempfile
    cwd = os.getcwd()
    tempdir = None
    try:
        tempdir = tempfile.mkdtemp(prefix='casautil')
        try:
            os.chdir(tempdir)
            sink = tools.logsink()
            sink.setlogfile(sanitize_unicode(os.devnull))
            try:
                os.unlink('casapy.log')
            except OSError as e:
                if e.errno != 2:
                    raise
        finally:
            os.chdir(cwd)
    finally:
        if tempdir is not None:
            shutil.rmtree(tempdir, onerror=_rmtree_error)
    sink.showconsole(True)
    sink.setglobal(True)
    sink.filter(sanitize_unicode(filter.upper()))
    return sink