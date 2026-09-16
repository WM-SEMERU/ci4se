def get_managed_configurations(self):
    res = {}
    if (self.sched.pushed_conf and self.cur_conf and 'instance_id' in self.
        cur_conf):
        res[self.cur_conf['instance_id']] = {'hash': self.cur_conf['hash'],
            'push_flavor': self.cur_conf['push_flavor'], 'managed_conf_id':
            self.cur_conf['managed_conf_id']}
    logger.debug('Get managed configuration: %s', res)
    return res