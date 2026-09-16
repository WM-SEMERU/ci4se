def _shouldOwn(self, param):
    if not (self.uid == param.parent and self.hasParam(param.name)):
        raise ValueError('Param %r does not belong to %r.' % (param, self))