def run_until(self, endtime, timeunit='minutes', save=True):
    integrator = self.case.solver.Integrator
    integrator.rununtil(endtime, timeunit)
    if save is True:
        self.case.save()