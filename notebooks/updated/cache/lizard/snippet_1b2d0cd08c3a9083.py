def fix_multiple_files(filenames, options, output=None):
    filenames = find_files(filenames, options.recursive, options.exclude)
    if options.jobs > 1:
        import multiprocessing
        pool = multiprocessing.Pool(options.jobs)
        pool.map(_fix_file, [(name, options) for name in filenames])
    else:
        for name in filenames:
            _fix_file((name, options, output))