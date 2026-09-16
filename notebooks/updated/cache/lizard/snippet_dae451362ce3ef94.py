def check_worker_health(self):
    self._logger.debug('Checking worker health.')
    workers = []
    restart_occurred = False
    for i, (worker, worker_t) in enumerate(self.worker_threads):
        if not self.environment.is_alive(worker_t):
            self._logger.warning('Worker %d died, restarting.', i + 1)
            worker = self._create_worker()
            worker_t = self._create_process(worker, 'Worker-%d' % (i + 1))
            worker_t.start()
            restart_occurred = True
        workers.append((worker, worker_t))
    if restart_occurred:
        self.worker_threads = workers
    else:
        self._logger.debug('Workers are up and running.')
    if not self.environment.is_alive(self.scheduler):
        self._logger.warning('Scheduler died, restarting.')
        scheduler = self._create_scheduler()
        self.scheduler = self._create_process(scheduler, 'Scheduler')
        self.scheduler.start()
    else:
        self._logger.debug('Scheduler is up and running.')
    return not restart_occurred