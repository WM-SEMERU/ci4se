def create_instance(self, name, moduleName, settings):
    if name in self.insts:
        raise ValueError("There's already an instance named %s" % name)
    if moduleName not in self.modules:
        raise ValueError("There's no module %s" % moduleName)
    md = self.modules[moduleName]
    deps = dict()
    for k, v in six.iteritems(md.deps):
        if k not in settings:
            settings[k] = self._get_or_create_a(v.type)
        if settings[k] is None:
            if not v.allow_null:
                raise ValueError("`null' not allowed for %s" % k)
        elif settings[k] not in self.insts:
            raise ValueError('No such instance %s' % settings[k])
        else:
            settings[k] = self.insts[settings[k]].object
            deps[k] = settings[k]
    for k, v in six.iteritems(md.vsettings):
        if k not in settings:
            settings[k] = v.default
            if v.default is None:
                self.l.warn('%s:%s not set' % (name, k))
    self.l.info('create_instance %-15s %s' % (name, md.implementedBy))
    cl = get_by_path(md.implementedBy)
    il = logging.getLogger(name)
    obj = cl(settings, il)
    self.register_instance(name, moduleName, obj, settings, deps)
    return obj