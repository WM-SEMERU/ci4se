def initialize_extensions(shell, extensions):
    try:
        iter(extensions)
    except TypeError:
        pass
    else:
        for ext in extensions:
            try:
                shell.extension_manager.load_extension(ext)
            except:
                ipy_utils.warn.warn('Error in loading extension: %s' % ext +
                    """
Check your config files in %s""" % ipy_utils.path.
                    get_ipython_dir())
                shell.showtraceback()