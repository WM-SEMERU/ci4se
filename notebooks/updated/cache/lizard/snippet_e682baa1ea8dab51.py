def dump_results(self, success):
    system = self.system
    t, _ = elapsed()
    if success and not system.files.no_output:
        system.varout.dump_np_vars()
        _, s = elapsed(t)
        logger.info('Simulation data dumped in {:s}.'.format(s))