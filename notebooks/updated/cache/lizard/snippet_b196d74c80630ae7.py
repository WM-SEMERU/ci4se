def is_valid_filename(filename, return_ext=False):
    ext = Path(filename).suffixes
    if len(ext) > 2:
        logg.warn(
            """Your filename has more than two extensions: {}.
Only considering the two last: {}."""
            .format(ext, ext[-2:]))
        ext = ext[-2:]
    if len(ext) == 2 and ext[0][1:] in text_exts and ext[1][1:] in ('gz', 'bz2'
        ):
        return ext[0][1:] if return_ext else True
    elif ext and ext[-1][1:] in avail_exts:
        return ext[-1][1:] if return_ext else True
    elif ''.join(ext) == '.soft.gz':
        return 'soft.gz' if return_ext else True
    elif ''.join(ext) == '.mtx.gz':
        return 'mtx.gz' if return_ext else True
    elif return_ext:
        raise ValueError(
            """"{}" does not end on a valid extension.
Please, provide one of the available extensions.
{}
Text files with .gz and .bz2 extensions are also supported."""
            .format(filename, avail_exts))
    else:
        return False