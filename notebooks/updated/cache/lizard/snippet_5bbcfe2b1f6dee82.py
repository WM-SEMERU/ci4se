def compress_for_rename(paths):
    case_map = dict((os.path.normcase(p), p) for p in paths)
    remaining = set(case_map)
    unchecked = sorted(set(os.path.split(p)[0] for p in case_map.values()),
        key=len)
    wildcards = set()

    def norm_join(*a):
        return os.path.normcase(os.path.join(*a))
    for root in unchecked:
        if any(os.path.normcase(root).startswith(w) for w in wildcards):
            continue
        all_files = set()
        all_subdirs = set()
        for dirname, subdirs, files in os.walk(root):
            all_subdirs.update(norm_join(root, dirname, d) for d in subdirs)
            all_files.update(norm_join(root, dirname, f) for f in files)
        if not all_files - remaining:
            remaining.difference_update(all_files)
            wildcards.add(root + os.sep)
    return set(map(case_map.__getitem__, remaining)) | wildcards