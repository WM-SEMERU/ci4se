def spawn_worker(self, entrypoint, args, kwargs, context_data=None,
    handle_result=None):
    if self._being_killed:
        _log.info('Worker spawn prevented due to being killed')
        raise ContainerBeingKilled()
    service = self.service_cls()
    worker_ctx = WorkerContext(self, service, entrypoint, args, kwargs,
        data=context_data)
    _log.debug('spawning %s', worker_ctx)
    gt = self._worker_pool.spawn(self._run_worker, worker_ctx, handle_result)
    gt.link(self._handle_worker_thread_exited, worker_ctx)
    self._worker_threads[worker_ctx] = gt
    return worker_ctx