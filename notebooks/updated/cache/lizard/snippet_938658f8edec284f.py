def rmi(self, force=False, via_name=False):
    identifier = self.get_full_name() if via_name else self._id or self.get_id(
        )
    cmdline = ['podman', 'rmi', identifier, '--force' if force else '']
    run_cmd(cmdline)