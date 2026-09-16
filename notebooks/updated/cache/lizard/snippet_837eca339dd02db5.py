def _read_apps(self):
    apps = {}
    for cfgfile in glob.iglob(os.path.join(self.confdir, '*.conf')):
        name = os.path.basename(cfgfile)[0:-5]
        try:
            app = AppLogParser(name, cfgfile, self.args, self.logdir, self.
                fields, self.name_cache, self.report)
        except (LogRaptorOptionError, LogRaptorConfigError, LogFormatError
            ) as err:
            logger.error('cannot add app %r: %s', name, err)
        else:
            apps[name] = app
    if not apps:
        raise LogRaptorConfigError('no configured application in %r!' %
            self.confdir)
    return apps