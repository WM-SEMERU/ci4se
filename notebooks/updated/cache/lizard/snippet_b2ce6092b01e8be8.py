def list_greps(self, repo, packages):
    pkg_list, pkg_size = [], []
    for line in packages.splitlines():
        if repo == 'sbo':
            if line.startswith('SLACKBUILD NAME: '):
                pkg_list.append(line[17:].strip())
                pkg_size.append('0 K')
        else:
            if line.startswith('PACKAGE NAME: '):
                pkg_list.append(line[15:].strip())
            if line.startswith('PACKAGE SIZE (compressed): '):
                pkg_size.append(line[26:].strip())
    if repo == 'alien' or repo == 'ktown':
        return alien_filter(pkg_list, pkg_size)
    return pkg_list, pkg_size