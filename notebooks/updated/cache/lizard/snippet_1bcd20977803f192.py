def createCleanup(self, varBind, **context):
    name, val = varBind
    debug.logger & debug.FLAG_INS and debug.logger(
        '%s: createCleanup(%s, %r)' % (self, name, val))
    instances = context['instances'].setdefault(self.name, {self.ST_CREATE:
        {}, self.ST_DESTROY: {}})
    idx = context['idx']
    self.branchVersionId += 1
    instances[self.ST_CREATE].pop(-idx - 1, None)
    self._vars[name].writeCleanup(varBind, **context)