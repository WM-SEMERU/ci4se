def set_target(self, target, ctx=None):
    if target is not None:
        if is_intercepted(target):
            self._interception = target
            self.target, self.ctx = get_intercepted(target)
        else:
            self.apply_pointcut(target, ctx=ctx)