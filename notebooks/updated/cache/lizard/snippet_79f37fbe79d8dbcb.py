def configure(self, cfg, handler, path=''):
    for name, attr in handler.attributes():
        if cfg.get(name) is not None:
            continue
        if attr.expected_type not in [list, dict]:
            cfg[name] = self.set(handler, attr, name, path, cfg)
        elif attr.default is None and not hasattr(handler, 'configure_%s' %
            name):
            self.action_required.append(('%s.%s: %s' % (path, name, attr.
                help_text)).strip('.'))
    for name, attr in handler.attributes():
        if cfg.get(name) is not None:
            continue
        if hasattr(handler, 'configure_%s' % name):
            fn = getattr(handler, 'configure_%s' % name)
            fn(self, cfg, '%s.%s' % (path, name))
            if attr.expected_type in [list, dict] and not cfg.get(name):
                try:
                    del cfg[name]
                except KeyError:
                    pass