def post_run_hook(self, func, prefix=None):
    cf = self.capture(func, prefix=prefix)
    self.post_run_hooks.append(cf)
    return cf