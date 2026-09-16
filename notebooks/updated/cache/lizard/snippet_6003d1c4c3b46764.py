def remove_file(fpath, verbose=None, ignore_errors=True, dryrun=False,
    quiet=QUIET):
    if verbose is None:
        verbose = not quiet
    if dryrun:
        if verbose:
            print('[util_path] Dryrem %r' % fpath)
        return
    else:
        try:
            os.remove(fpath)
            if verbose:
                print('[util_path] Removed %r' % fpath)
        except OSError:
            print('[util_path.remove_file] Misrem %r' % fpath)
            if not ignore_errors:
                raise
            return False
    return True