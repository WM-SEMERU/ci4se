def register_module_alias(self, alias, module_path, after_init=False):
    command = 'post-pymodule-alias' if after_init else 'pymodule-alias'
    self._set(command, '%s=%s' % (alias, module_path), multi=True)
    return self._section