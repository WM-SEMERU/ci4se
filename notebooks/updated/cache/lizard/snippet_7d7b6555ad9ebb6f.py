def process_pool(self, limited_run=False):
    from multiprocessing import cpu_count
    from ambry.bundle.concurrent import Pool, init_library
    if self.processes:
        cpus = self.processes
    else:
        cpus = cpu_count()
    self.logger.info('Starting MP pool with {} processors'.format(cpus))
    return Pool(self, processes=cpus, initializer=init_library,
        maxtasksperchild=1, initargs=[self.database.dsn, self.
        _account_password, limited_run])