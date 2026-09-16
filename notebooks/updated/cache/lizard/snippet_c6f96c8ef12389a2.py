def add_hookspecs(self, module_or_class):
    names = []
    for name in dir(module_or_class):
        spec_opts = self.parse_hookspec_opts(module_or_class, name)
        if spec_opts is not None:
            hc = getattr(self.hook, name, None)
            if hc is None:
                hc = _HookCaller(name, self._hookexec, module_or_class,
                    spec_opts)
                setattr(self.hook, name, hc)
            else:
                hc.set_specification(module_or_class, spec_opts)
                for hookfunction in hc.get_hookimpls():
                    self._verify_hook(hc, hookfunction)
            names.append(name)
    if not names:
        raise ValueError('did not find any %r hooks in %r' % (self.
            project_name, module_or_class))