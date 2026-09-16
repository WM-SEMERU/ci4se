def __get_managed_files_dpkg(self):
    dirs = set()
    links = set()
    files = set()
    for pkg_name in salt.utils.stringutils.to_str(self._syscall(
        'dpkg-query', None, None, '-Wf', '${binary:Package}\\n')[0]).split(os
        .linesep):
        pkg_name = pkg_name.strip()
        if not pkg_name:
            continue
        for resource in salt.utils.stringutils.to_str(self._syscall('dpkg',
            None, None, '-L', pkg_name)[0]).split(os.linesep):
            resource = resource.strip()
            if not resource or resource in ['/', './', '.']:
                continue
            if os.path.isdir(resource):
                dirs.add(resource)
            elif os.path.islink(resource):
                links.add(resource)
            elif os.path.isfile(resource):
                files.add(resource)
    return sorted(files), sorted(dirs), sorted(links)