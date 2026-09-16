def heartbeat(self):
    self.thread_debug('heartbeat')
    if self.last_stats:
        if self.stats.http_run <= self.last_stats.http_run:
            self.NOTIFY('No monitors run since last heartbeat!', service=
                'heartbeat')
            return
        elif self.stats.http_handled <= self.last_stats.http_handled:
            self.NOTIFY('No monitor results handled since last heartbeat!',
                service='heartbeat')
            return
    if self.config.get('heartbeat-hook'):
        result = requests.get(self.config.get('heartbeat-hook'))
        if result.status_code != 200:
            self.NOTIFY('Heartbeat ping to statuscake failed!', level='ERROR')
    self.last_stats = self.stats.copy()