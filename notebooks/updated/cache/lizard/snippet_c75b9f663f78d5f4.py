def load_module(self, name):
    if name in sys.modules:
        return sys.modules[name]
    raise DisabledIncludeError(
        'Include type %r disabled, cannot import module %r' % (self.
        _module_prefix, name))