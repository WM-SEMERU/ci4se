def update(self, process_list):
    logger.debug('{}: Update stats using service {}'.format(self.NAME, self
        .get('service_cmd')))
    try:
        res = check_output(self.get('service_cmd').split(), stderr=STDOUT
            ).decode('utf-8')
    except OSError as e:
        logger.debug('{}: Error while executing service ({})'.format(self.
            NAME, e))
    else:
        status = {'running': 0, 'stopped': 0, 'upstart': 0}
        for r in res.split('\n'):
            l = r.split()
            if len(l) < 4:
                continue
            if l[1] == '+':
                status['running'] += 1
            elif l[1] == '-':
                status['stopped'] += 1
            elif l[1] == '?':
                status['upstart'] += 1
        output = 'Services\n'
        for k, v in iteritems(status):
            output += '{}: {}\n'.format(k, v)
        self.set_result(output, separator=' ')
    return self.result()