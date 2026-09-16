def wheel_libs(wheel_fname, filt_func=None):
    with TemporaryDirectory() as tmpdir:
        zip2dir(wheel_fname, tmpdir)
        lib_dict = tree_libs(tmpdir, filt_func)
    return stripped_lib_dict(lib_dict, realpath(tmpdir) + os.path.sep)