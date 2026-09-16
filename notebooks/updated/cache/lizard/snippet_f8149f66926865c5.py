def new_tracer(self, io_loop=None):
    channel = self._create_local_agent_channel(io_loop=io_loop)
    sampler = self.sampler
    if not sampler:
        sampler = RemoteControlledSampler(channel=channel, service_name=
            self.service_name, logger=logger, metrics_factory=self.
            _metrics_factory, error_reporter=self.error_reporter,
            sampling_refresh_interval=self.sampling_refresh_interval,
            max_operations=self.max_operations)
    logger.info('Using sampler %s', sampler)
    reporter = Reporter(channel=channel, queue_capacity=self.
        reporter_queue_size, batch_size=self.reporter_batch_size,
        flush_interval=self.reporter_flush_interval, logger=logger,
        metrics_factory=self._metrics_factory, error_reporter=self.
        error_reporter)
    if self.logging:
        reporter = CompositeReporter(reporter, LoggingReporter(logger))
    if not self.throttler_group() is None:
        throttler = RemoteThrottler(channel, self.service_name,
            refresh_interval=self.throttler_refresh_interval, logger=logger,
            metrics_factory=self._metrics_factory, error_reporter=self.
            error_reporter)
    else:
        throttler = None
    return self.create_tracer(reporter=reporter, sampler=sampler, throttler
        =throttler)