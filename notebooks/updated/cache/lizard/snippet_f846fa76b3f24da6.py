def _check_guts_toc(attr, old, toc, last_build, pyc=0):
    return _check_guts_eq(attr, old, toc, last_build) or _check_guts_toc_mtime(
        attr, old, toc, last_build, pyc=pyc)