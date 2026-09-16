def stop(self):
    args = self.getShutdownArgs() + ['shutdown']
    Pyro.nsc.main(args)
    self.join()