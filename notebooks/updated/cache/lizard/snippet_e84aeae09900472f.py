async def run(self):
    logger.info(__("Starting Resolwe listener on channel '{}'.", state.
        MANAGER_EXECUTOR_CHANNELS.queue))
    while not self._should_stop:
        await self.push_stats()
        ret = await self._call_redis(aioredis.Redis.blpop, state.
            MANAGER_EXECUTOR_CHANNELS.queue, timeout=1)
        if ret is None:
            self.load_avg.add(0)
            continue
        remaining = await self._call_redis(aioredis.Redis.llen, state.
            MANAGER_EXECUTOR_CHANNELS.queue)
        self.load_avg.add(remaining + 1)
        self.check_critical_load()
        _, item = ret
        try:
            item = item.decode('utf-8')
            logger.debug(__('Got command from executor: {}', item))
            obj = json.loads(item)
        except json.JSONDecodeError:
            logger.error(__('Undecodable command packet:\n\n{}'), traceback
                .format_exc())
            continue
        command = obj.get(ExecutorProtocol.COMMAND, None)
        if command is None:
            continue
        service_start = time.perf_counter()
        handler = getattr(self, 'handle_' + command, None)
        if handler:
            try:
                with PrioritizedBatcher.global_instance():
                    await database_sync_to_async(handler)(obj)
            except Exception:
                logger.error(__('Executor command handling error:\n\n{}',
                    traceback.format_exc()))
        else:
            logger.error(__("Unknown executor command '{}'.", command),
                extra={'decoded_packet': obj})
        service_end = time.perf_counter()
        self.service_time.update(service_end - service_start)
    logger.info(__("Stopping Resolwe listener on channel '{}'.", state.
        MANAGER_EXECUTOR_CHANNELS.queue))