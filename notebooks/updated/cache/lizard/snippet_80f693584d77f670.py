def get_plugin_folders():
    folders = []
    defaultfolder = normpath('~/.linkchecker/plugins')
    if not os.path.exists(defaultfolder) and not Portable:
        try:
            make_userdir(defaultfolder)
        except Exception as errmsg:
            msg = _('could not create plugin directory %(dirname)r: %(errmsg)r'
                )
            args = dict(dirname=defaultfolder, errmsg=errmsg)
            log.warn(LOG_CHECK, msg % args)
    if os.path.exists(defaultfolder):
        folders.append(defaultfolder)
    return folders