def _checks(self, do_checks=False, do_actions=False, poller_tags=None,
    reactionner_tags=None, worker_name='none', module_types=None):
    if poller_tags is None:
        poller_tags = ['None']
    if reactionner_tags is None:
        reactionner_tags = ['None']
    if module_types is None:
        module_types = ['fork']
    do_checks = do_checks == 'True'
    do_actions = do_actions == 'True'
    res = self.app.sched.get_to_run_checks(do_checks, do_actions,
        poller_tags, reactionner_tags, worker_name, module_types)
    return serialize(res, True)