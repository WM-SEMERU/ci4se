def add_final_live(self, print_progress=True, print_func=None):
    if print_func is None:
        print_func = print_fn
    ncall = self.ncall
    it = self.it - 1
    for i, results in enumerate(self.add_live_points()):
        (worst, ustar, vstar, loglstar, logvol, logwt, logz, logzvar, h, nc,
            worst_it, boundidx, bounditer, eff, delta_logz) = results
        if delta_logz > 1000000.0:
            delta_logz = np.inf
        if logz <= -1000000.0:
            logz = -np.inf
        if print_progress:
            print_func(results, it, ncall, add_live_it=i + 1, dlogz=0.01)