def do_work_unit(self, args):
    work_spec_name = self._get_work_spec_name(args)
    for work_unit_name in args.unit:
        status = self.task_master.get_work_unit_status(work_spec_name,
            work_unit_name)
        self.stdout.write('{0} ({1!r})\n'.format(work_unit_name, status[
            'status']))
        if 'expiration' in status:
            when = time.ctime(status['expiration'])
            if status == 'available':
                if status['expiration'] == 0:
                    self.stdout.write('  Never scheduled\n')
                else:
                    self.stdout.write('  Available since: {0}\n'.format(when))
            else:
                self.stdout.write('  Expires: {0}\n'.format(when))
        if 'worker_id' in status:
            try:
                heartbeat = self.task_master.get_heartbeat(status['worker_id'])
            except:
                heartbeat = None
            if heartbeat:
                hostname = heartbeat.get('fqdn', None) or heartbeat.get(
                    'hostname', None) or ''
                ipaddrs = ', '.join(heartbeat.get('ipaddrs', ()))
                if hostname and ipaddrs:
                    summary = '{0} on {1}'.format(hostname, ipaddrs)
                else:
                    summary = hostname + ipaddrs
            else:
                summary = 'No information'
            self.stdout.write('  Worker: {0} ({1})\n'.format(status[
                'worker_id'], summary))
        if 'traceback' in status:
            self.stdout.write('  Traceback:\n{0}\n'.format(status['traceback'])
                )
        if 'depends_on' in status:
            self.stdout.write('  Depends on:\n')
            for what in status['depends_on']:
                self.stdout.write('    {0!r}\n'.format(what))