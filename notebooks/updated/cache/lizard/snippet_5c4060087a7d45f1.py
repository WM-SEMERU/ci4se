def is_new_osx():
    name = distutils.util.get_platform()
    if sys.platform != 'darwin':
        return False
    elif name.startswith('macosx-10'):
        minor_version = int(name.split('-')[1].split('.')[1])
        if minor_version >= 7:
            return True
        else:
            return False
    else:
        return False