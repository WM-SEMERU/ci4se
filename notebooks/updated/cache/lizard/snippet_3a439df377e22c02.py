def find_data_files(source, target, patterns):
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError('Magic not allowed in src, target')
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source, pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target, os.path.relpath(filename,
                    source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path, []).append(filename)
    return sorted(ret.items())