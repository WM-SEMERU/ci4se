def get_new_actions(self):
    _t0 = time.time()
    self.hook_point('get_new_actions')
    statsmgr.timer('hook.get-new-actions', time.time() - _t0)
    for elt in self.all_my_hosts_and_services():
        for action in elt.actions:
            logger.debug('Got a new action for %s: %s', elt, action)
            self.add(action)
        elt.actions = []