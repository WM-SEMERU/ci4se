def perform(self):
    db_versions = self.table.versions()
    version = self.version
    if version.is_processed(db_versions
        ) and not self.config.force_version == self.version.number:
        self.log('version {} is already installed'.format(version.number))
        return
    self.start()
    try:
        self._perform_version(version)
    except Exception:
        if sys.version_info < (3, 4):
            msg = traceback.format_exc().decode('utf8', errors='ignore')
        else:
            msg = traceback.format_exc()
        error = '\n'.join(self.logs + ['\n', msg])
        self.table.record_log(version.number, error)
        raise
    self.finish()