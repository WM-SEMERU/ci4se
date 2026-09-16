def site_data_dir(appname, appauthor=None, version=None):
    if sys.platform.startswith('win'):
        if appauthor is None:
            raise AppDirsError("must specify 'appauthor' on Windows")
        path = os.path.join(_get_win_folder('CSIDL_COMMON_APPDATA'),
            appauthor, appname)
    elif sys.platform == 'darwin':
        path = os.path.join(os.path.expanduser(
            '/Library/Application Support'), appname)
    else:
        path = '/etc/xdg/' + appname.lower()
    if version:
        path = os.path.join(path, version)
    return path