def _update_targets(self):
    hostname = self.opts.get('tgt', '')
    if '@' in hostname:
        user, hostname = hostname.split('@', 1)
    else:
        user = self.opts.get('ssh_user')
    if hostname == '*':
        hostname = ''
    if salt.utils.network.is_reachable_host(hostname):
        hostname = salt.utils.network.ip_to_host(hostname)
        self.opts['tgt'] = hostname
        self.targets[hostname] = {'passwd': self.opts.get('ssh_passwd', ''),
            'host': hostname, 'user': user}
        if self.opts.get('ssh_update_roster'):
            self._update_roster()