def run(self, context: ActionContext):
    iterator = itertools.count(start=self.start, step=self.step)
    for i in iterator:
        self.with_iteration(i)
        if self.stop is not None and i >= self.stop:
            break
        try:
            self._action(context)
        except Loop.Continue:
            continue
        except Loop.Break:
            break