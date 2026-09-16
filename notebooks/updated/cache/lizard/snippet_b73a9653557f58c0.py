def _cache(cpath, arg):
    if not os.path.isdir(cpath):
        os.makedirs(cpath)
    for k, v in six.iteritems(arg):
        save(os.path.join(cpath, k + '.pp'), v, create_directories=True,
            overwrite=True)
    return True