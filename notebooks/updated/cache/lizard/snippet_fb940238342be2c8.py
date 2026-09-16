def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as err:
        if err.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            ui.error(c.MESSAGES['path_unmakable'], err)
            sys.exit(1)