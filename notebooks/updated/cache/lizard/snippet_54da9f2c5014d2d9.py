def collect_internal_data(self):
    section = 'configuration'
    self.out.put(section)
    self.collector.add(section)
    self.out.put('Saving config', indent=2)
    self.collector.write('General Configuration', self.config)
    self.out.put('Saving pillars', indent=2)
    self.collector.write('Active Pillars', self._local_call({'fun':
        'pillar.items'}))
    section = 'highstate'
    self.out.put(section)
    self.collector.add(section)
    self.out.put('Saving highstate', indent=2)
    self.collector.write('Rendered highstate', self._local_call({'fun':
        'state.show_highstate'}))