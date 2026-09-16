def assert_compile_finished(app_folder):
    fpath = os.path.join(app_folder, '.postbuild.flag')
    if not os.path.isfile(fpath):
        msg = (
            'No postbuild flag set, LXC container may have crashed while building. Check compile logs for build.'
            )
        raise AssertionError(msg)
    try:
        os.remove(fpath)
    except OSError:
        pass