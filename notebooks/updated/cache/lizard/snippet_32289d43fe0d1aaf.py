def search(path, pattern, flags=8, bufsize=1, ignore_if_missing=False,
    multiline=False):
    if multiline:
        flags = _add_flags(flags, 'MULTILINE')
        bufsize = 'file'
    return replace(path, pattern, '', flags=flags, bufsize=bufsize, dry_run
        =True, search_only=True, show_changes=False, ignore_if_missing=
        ignore_if_missing)