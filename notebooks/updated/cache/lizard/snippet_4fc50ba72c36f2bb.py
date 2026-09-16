def tune_in(self):
    self._spawn_syndics()
    self.local = salt.client.get_local_client(self.opts['_minion_conf_file'
        ], io_loop=self.io_loop)
    self.local.event.subscribe('')
    log.debug("SyndicManager '%s' trying to tune in", self.opts['id'])
    self.job_rets = {}
    self.raw_events = []
    self._reset_event_aggregation()
    future = self.local.event.set_event_handler(self._process_event)
    self.io_loop.add_future(future, self.reconnect_event_bus)
    self.forward_events = tornado.ioloop.PeriodicCallback(self.
        _forward_events, self.opts['syndic_event_forward_timeout'] * 1000)
    self.forward_events.start()
    enable_sigusr1_handler()
    self.io_loop.start()