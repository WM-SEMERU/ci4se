def run(self, data, runtime_dir, argv):
    process_scheduling = self.scheduling_class_map[data.process.
        scheduling_class]
    if 'DISPATCHER_MAPPING' in getattr(settings, 'FLOW_MANAGER', {}):
        class_name = settings.FLOW_MANAGER['DISPATCHER_MAPPING'][
            process_scheduling]
    else:
        class_name = getattr(settings, 'FLOW_MANAGER', {}).get('NAME',
            DEFAULT_CONNECTOR)
    data.scheduled = now()
    data.save(update_fields=['scheduled'])
    async_to_sync(self.sync_counter.inc)('executor')
    return self.connectors[class_name].submit(data, runtime_dir, argv)