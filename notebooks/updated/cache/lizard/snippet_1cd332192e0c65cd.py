def add_log_options(self, verbose_func=None, quiet_func=None):
    if not verbose_func:

        def verbose_func():
            return log.config(verbose=True)
    if not quiet_func:

        def quiet_func():
            return log.config(quiet=True)
    self.option('-v, --verbose', 'show more logs', verbose_func)
    self.option('-q, --quiet', 'show less logs', quiet_func)
    return self