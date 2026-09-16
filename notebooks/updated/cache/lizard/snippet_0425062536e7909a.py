def get_daemon_stats(self, details=False):
    res = self.get_id()
    res.update({'program_start': self.program_start, 'spare': self.spare,
        'counters': {}, 'metrics': [], 'modules': {'internal': {},
        'external': {}}})
    modules = res['modules']
    counters = res['counters']
    counters['modules'] = len(self.modules_manager.instances)
    for instance in self.modules_manager.get_internal_instances():
        state = {True: 'ok', False: 'stopped'}[instance not in self.
            modules_manager.to_restart]
        modules['internal'][instance.name] = {'name': instance.name,
            'state': state}
    for instance in self.modules_manager.get_external_instances():
        state = {True: 'ok', False: 'stopped'}[instance not in self.
            modules_manager.to_restart]
        modules['internal'][instance.name] = {'name': instance.name,
            'state': state}
    return res