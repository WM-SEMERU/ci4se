def add_runnable(self, runnable):
    if runnable.id in self.runnables:
        raise SimError('Duplicate runnable component {0}'.format(runnable.id))
    self.runnables[runnable.id] = runnable