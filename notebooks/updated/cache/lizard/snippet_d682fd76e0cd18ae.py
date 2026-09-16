def _match_real(filename, include, exclude, follow, symlinks):
    sep = '\\' if util.platform() == 'windows' else '/'
    if isinstance(filename, bytes):
        sep = os.fsencode(sep)
    if not filename.endswith(sep) and os.path.isdir(filename):
        filename += sep
    matched = False
    for pattern in include:
        if _fs_match(pattern, filename, sep, follow, symlinks):
            matched = True
            break
    if matched:
        matched = True
        if exclude:
            for pattern in exclude:
                if _fs_match(pattern, filename, sep, follow, symlinks):
                    matched = False
                    break
    return matched