def setWritePrivs(fname, makeWritable, ignoreErrors=False):
    privs = os.stat(fname).st_mode
    try:
        if makeWritable:
            os.chmod(fname, privs | stat.S_IWUSR)
        else:
            os.chmod(fname, privs & ~stat.S_IWUSR)
    except OSError:
        if ignoreErrors:
            pass
        else:
            raise