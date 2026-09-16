def _find_rule_no(self, mac):
    ipt_cmd = ['iptables', '-L', '--line-numbers']
    cmdo = dsl.execute(ipt_cmd, self._root_helper, log_output=False)
    for o in cmdo.split('\n'):
        if mac in o.lower():
            rule_no = o.split()[0]
            LOG.info('Found rule %(rule)s for %(mac)s.', {'rule': rule_no,
                'mac': mac})
            return rule_no