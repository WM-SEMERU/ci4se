def collect(self):
    try:
        if str_to_bool(self.config['use_sudo']):
            cmdline = [self.config['sudo_exe'], '-u', self.config[
                'sudo_user'], '--', self.config['amavisd_exe'], '-c', '1']
        else:
            cmdline = [self.config['amavisd_exe'], '-c', '1']
        agent = subprocess.Popen(cmdline, stdout=subprocess.PIPE)
        agent_out = agent.communicate()[0]
        lines = agent_out.strip().split(os.linesep)
        for line in lines:
            for rex in self.matchers:
                res = rex.match(line)
                if res:
                    groups = res.groupdict()
                    name = groups['name']
                    for metric, value in groups.items():
                        if metric == 'name':
                            continue
                        mtype = 'GAUGE'
                        precision = 2
                        if metric in ('count', 'time'):
                            mtype = 'COUNTER'
                            precision = 0
                        self.publish('{}.{}'.format(name, metric), value,
                            metric_type=mtype, precision=precision)
    except OSError as err:
        self.log.error('Could not run %s: %s', self.config['amavisd_exe'], err)
        return None
    return True