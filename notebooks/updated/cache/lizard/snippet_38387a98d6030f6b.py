def set_mode(filename, flags):
    try:
        mode = os.lstat(filename).st_mode
    except OSError:
        return
    if not mode & flags:
        try:
            os.chmod(filename, flags | mode)
        except OSError as msg:
            log_error("could not set mode flags for `%s': %s" % (filename, msg)
                )