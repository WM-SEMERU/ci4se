def file_uptodate(fname, cmp_fname):
    try:
        return file_exists(fname) and file_exists(cmp_fname
            ) and os.path.getmtime(fname) >= os.path.getmtime(cmp_fname)
    except OSError:
        return False