def run_nose(self, params):
    thread.set_index(params.thread_index)
    log.debug('[%s] Starting nose iterations: %s', params.worker_index, params)
    assert isinstance(params.tests, list)
    end_time = self.params.ramp_up + self.params.hold_for
    end_time += time.time() if end_time else 0
    time.sleep(params.delay)
    plugin = ApiritifPlugin(self._writer)
    self._writer.concurrency += 1
    config = Config(env=os.environ, files=all_config_files(), plugins=
        DefaultPluginManager())
    config.plugins.addPlugins(extraplugins=[plugin])
    config.testNames = params.tests
    config.verbosity = 3 if params.verbose else 0
    if params.verbose:
        config.stream = open(os.devnull, 'w')
    iteration = 0
    try:
        while True:
            log.debug('Starting iteration:: index=%d,start_time=%.3f',
                iteration, time.time())
            thread.set_iteration(iteration)
            ApiritifTestProgram(config=config)
            log.debug('Finishing iteration:: index=%d,end_time=%.3f',
                iteration, time.time())
            iteration += 1
            if plugin.stop_reason:
                log.debug('[%s] finished prematurely: %s', params.
                    worker_index, plugin.stop_reason)
            elif iteration >= params.iterations:
                log.debug('[%s] iteration limit reached: %s', params.
                    worker_index, params.iterations)
            elif 0 < end_time <= time.time():
                log.debug('[%s] duration limit reached: %s', params.
                    worker_index, params.hold_for)
            else:
                continue
            break
    finally:
        self._writer.concurrency -= 1
        if params.verbose:
            config.stream.close()