def call_command(self, cmdname, **kw):
    for dirname in INSTALL_DIRECTORY_ATTRS:
        kw.setdefault(dirname, self.bdist_dir)
    kw.setdefault('skip_build', self.skip_build)
    kw.setdefault('dry_run', self.dry_run)
    cmd = self.reinitialize_command(cmdname, **kw)
    self.run_command(cmdname)
    return cmd