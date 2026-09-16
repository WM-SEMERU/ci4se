def _determine_froms(addon_package, path):
    if path.startswith('~/'):
        path_tail = path[2:]
        from_tail = join('home', 'USERNAME', path_tail)
    else:
        from_tail = path.lstrip(os.sep)
    from_default = join(addon_package.default_files_basedir, from_tail)
    from_custom = join(addon_package.custom_files_basedir, from_tail)
    return from_custom, from_default