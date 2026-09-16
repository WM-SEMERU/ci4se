def initialize(self, init=initializer.Uniform(), ctx=None, verbose=False,
    force_reinit=False):
    if verbose:
        init.set_verbosity(verbose=verbose)
    for _, v in self.items():
        v.initialize(None, ctx, init, force_reinit=force_reinit)