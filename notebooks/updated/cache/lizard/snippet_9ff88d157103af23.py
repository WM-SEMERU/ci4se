def _is_used_deprecated(self):
    func_path = '{m_name}.{f_name}'.format(m_name=self._globals.get(self.
        MODULE_NAME, '') or self._globals['__name__'].split('.')[-1],
        f_name=self._orig_f_name)
    return func_path in self._globals.get('__opts__').get(self.
        CFG_USE_DEPRECATED, list()) or func_path in self._globals.get(
        '__pillar__').get(self.CFG_USE_DEPRECATED, list()
        ) or self._policy == self.OPT_IN and not func_path in self._globals.get(
        '__opts__', {}).get(self.CFG_USE_SUPERSEDED, list()
        ) and not func_path in self._globals.get('__pillar__', {}).get(self
        .CFG_USE_SUPERSEDED, list()), func_path