def compute_We(self, Eemin=None, Eemax=None):
    if Eemin is None and Eemax is None:
        We = self.We
    else:
        if Eemax is None:
            Eemax = self.Eemax
        if Eemin is None:
            Eemin = self.Eemin
        log10gmin = np.log10(Eemin / mec2).value
        log10gmax = np.log10(Eemax / mec2).value
        gam = np.logspace(log10gmin, log10gmax, int(self.nEed * (log10gmax -
            log10gmin)))
        nelec = self.particle_distribution(gam * mec2).to(1 / mec2_unit).value
        We = trapz_loglog(gam * nelec, gam * mec2)
    return We