def _mkstemp_inner(dir, pre, suf, flags):
    names = _get_candidate_names()
    for seq in range(TMP_MAX):
        name = next(names)
        file = _os.path.join(dir, pre + name + suf)
        try:
            fd = _os.open(file, flags, 384)
            return fd, _os.path.abspath(file)
        except FileExistsError:
            continue
        except PermissionError:
            if _os.name == 'nt':
                continue
            else:
                raise
    raise FileExistsError(_errno.EEXIST, 'No usable temporary file name found')