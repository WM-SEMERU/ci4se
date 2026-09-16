def __setup():
    global __collaborators, __flag_first
    import f311
    __flag_first = False
    for pkgname in f311.COLLABORATORS_C:
        try:
            pkg = importlib.import_module(pkgname)
            a99.get_python_logger().info("Imported collaborator package '{}'"
                .format(pkgname))
            try:
                if hasattr(pkg, '_setup_filetypes'):
                    pkg._setup_filetypes()
                else:
                    _collect_classes(pkg)
                __collaborators[pkgname] = pkg
            except:
                a99.get_python_logger().exception(
                    "Actually, package '{}' gave error".format(pkgname))
                raise
        except:
            a99.get_python_logger().warning("Failed to import package '{}".
                format(pkgname))