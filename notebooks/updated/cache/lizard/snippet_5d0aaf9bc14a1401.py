def set_permissions(self, owner, file_perms=PERMS_FILE_DEFAULT, dir_perms=
    PERMS_DIR_DEFAULT, use_sudo=True):
    runner = self._runner.sudo if use_sudo else self._runner.run
    if use_sudo:
        runner("chown -R '{0}' '{1}'".format(owner, self._base))
    for path in (self._base, self._releases):
        runner("chmod '{0}' '{1}'".format(dir_perms, path))
    runner("chmod -R '{0}' '{1}'".format(file_perms, self._base))