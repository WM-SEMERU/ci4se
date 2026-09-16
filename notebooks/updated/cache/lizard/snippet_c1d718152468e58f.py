def pluginPackagePaths(name):
    package = name.split('.')
    return [os.path.abspath(os.path.join(x, *package)) for x in sys.path if
        not os.path.exists(os.path.join(x, *(package + ['__init__.py'])))]