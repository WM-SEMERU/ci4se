def build_single_handler_application(path, argv=None):
    argv = argv or []
    path = os.path.abspath(path)
    if os.path.isdir(path):
        handler = DirectoryHandler(filename=path, argv=argv)
    elif os.path.isfile(path):
        if path.endswith('.ipynb'):
            handler = NotebookHandler(filename=path, argv=argv)
        elif path.endswith('.py'):
            if path.endswith('main.py'):
                warnings.warn(DIRSTYLE_MAIN_WARNING)
            handler = ScriptHandler(filename=path, argv=argv)
        else:
            raise ValueError(
                "Expected a '.py' script or '.ipynb' notebook, got: '%s'" %
                path)
    else:
        raise ValueError(
            'Path for Bokeh server application does not exist: %s' % path)
    if handler.failed:
        raise RuntimeError('Error loading %s:\n\n%s\n%s ' % (path, handler.
            error, handler.error_detail))
    application = Application(handler)
    return application