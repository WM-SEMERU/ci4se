def read(self, files=None):
    if files is None:
        cfiles = []
    else:
        cfiles = files[:]
    if not cfiles:
        userconf = get_user_config()
        if os.path.isfile(userconf):
            cfiles.append(userconf)
    filtered_cfiles = []
    for cfile in cfiles:
        if not os.path.isfile(cfile):
            log.warn(LOG_CHECK, _('Configuration file %r does not exist.'),
                cfile)
        elif not fileutil.is_readable(cfile):
            log.warn(LOG_CHECK, _('Configuration file %r is not readable.'),
                cfile)
        else:
            filtered_cfiles.append(cfile)
    log.debug(LOG_CHECK, 'reading configuration from %s', filtered_cfiles)
    confparse.LCConfigParser(self).read(filtered_cfiles)