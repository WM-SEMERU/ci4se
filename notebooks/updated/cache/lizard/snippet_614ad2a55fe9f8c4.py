def get_executor(self, create=1):
    try:
        executor = self.executor
    except AttributeError:
        if not create:
            raise
        try:
            act = self.builder.action
        except AttributeError:
            executor = SCons.Executor.Null(targets=[self])
        else:
            executor = SCons.Executor.Executor(act, self.env or self.
                builder.env, [self.builder.overrides], [self], self.sources)
        self.executor = executor
    return executor