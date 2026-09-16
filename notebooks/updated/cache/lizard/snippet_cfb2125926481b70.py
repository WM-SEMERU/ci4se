def clock(self, interval, basis):
    cache_name = self._classify_clock(interval, basis)
    cache_data = self.clock_cache.get(cache_name)
    if cache_data is None:
        parent_stream, trigger = self.parent.clock(interval, basis)
        if trigger.use_count is False:
            raise SensorGraphSemanticError(
                'Unsupported clock trigger in GatedClockScope', trigger=trigger
                )
        elif interval % trigger.reference != 0:
            raise SensorGraphSemanticError(
                'Unsupported trigger ratio in GatedClockScope', trigger=
                trigger, interval=interval)
        ratio = interval // trigger.reference
        stream = self.allocator.allocate_stream(DataStream.CounterType)
        latch_stream = self.allocator.attach_stream(self.latch_stream)
        self.sensor_graph.add_node(
            '({} always && {} {}) => {} using copy_latest_a'.format(
            parent_stream, latch_stream, self.latch_trigger, stream))
        self.clock_cache[cache_name] = stream, ratio
    else:
        stream, ratio = cache_data
    if interval % ratio != 0:
        raise SensorGraphSemanticError(
            'Unsupported trigger ratio in GatedClockScope', ratio=ratio,
            interval=interval)
    count = interval // ratio
    clock_stream = self.allocator.attach_stream(stream)
    return clock_stream, InputTrigger('count', '>=', count)