def glob_by_extensions(directory, extensions):
    directorycheck(directory)
    files = []
    xt = files.extend
    for ex in extensions:
        xt(glob.glob('{0}/*.{1}'.format(directory, ex)))
    return files