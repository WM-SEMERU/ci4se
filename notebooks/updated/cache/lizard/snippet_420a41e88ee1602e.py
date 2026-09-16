def _glob1(self, pattern, ondisk=True, source=False, strings=False):
    search_dir_list = self.get_all_rdirs()
    for srcdir in self.srcdir_list():
        search_dir_list.extend(srcdir.get_all_rdirs())
    selfEntry = self.Entry
    names = []
    for dir in search_dir_list:
        node_names = [v.name for k, v in dir.entries.items() if k not in (
            '.', '..')]
        names.extend(node_names)
        if not strings:
            for name in node_names:
                selfEntry(name)
        if ondisk:
            try:
                disk_names = os.listdir(dir._abspath)
            except os.error:
                continue
            names.extend(disk_names)
            if not strings:
                if pattern[0] != '.':
                    disk_names = [x for x in disk_names if x[0] != '.']
                disk_names = fnmatch.filter(disk_names, pattern)
                dirEntry = dir.Entry
                for name in disk_names:
                    name = './' + name
                    node = dirEntry(name).disambiguate()
                    n = selfEntry(name)
                    if n.__class__ != node.__class__:
                        n.__class__ = node.__class__
                        n._morph()
    names = set(names)
    if pattern[0] != '.':
        names = [x for x in names if x[0] != '.']
    names = fnmatch.filter(names, pattern)
    if strings:
        return names
    return [self.entries[_my_normcase(n)] for n in names]