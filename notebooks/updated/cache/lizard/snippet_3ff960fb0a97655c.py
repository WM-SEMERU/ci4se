def _append_base_arguments(self):
    if self.exc and self.only:
        raise PackerException('Cannot provide both "except" and "only"')
    elif self.exc:
        self._add_opt('-except={0}'.format(self._join_comma(self.exc)))
    elif self.only:
        self._add_opt('-only={0}'.format(self._join_comma(self.only)))
    for var, value in self.vars.items():
        self._add_opt('-var')
        self._add_opt('{0}={1}'.format(var, value))
    if self.var_file:
        self._add_opt('-var-file={0}'.format(self.var_file))