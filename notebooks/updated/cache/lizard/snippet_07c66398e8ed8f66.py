def print_plugins(folders, exit_code=0):
    modules = plugins.get_plugin_modules(folders)
    pluginclasses = sorted(plugins.get_plugin_classes(modules), key=lambda
        x: x.__name__)
    for pluginclass in pluginclasses:
        print(pluginclass.__name__)
        doc = strformat.wrap(pluginclass.__doc__, 80)
        print(strformat.indent(doc))
        print()
    sys.exit(exit_code)