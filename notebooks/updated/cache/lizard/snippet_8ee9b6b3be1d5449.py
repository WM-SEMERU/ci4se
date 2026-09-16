def is_plugin_installed(name):
    for directory in plugin_paths:
        if isdir(join(directory, name)):
            return True
    return False