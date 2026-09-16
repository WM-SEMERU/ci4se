def _run_task(self, play, task, is_handler):
    self.callbacks.on_task_start(utils.template(play.basedir, task.name,
        task.module_vars, lookup_fatal=False), is_handler)
    results = self._run_task_internal(task)
    hosts_remaining = True
    if results is None:
        hosts_remaining = False
        results = {}
    contacted = results.get('contacted', {})
    self.stats.compute(results, ignore_errors=task.ignore_errors)
    for host, result in contacted.iteritems():
        if result.get('skipped', False):
            continue
        facts = result.get('ansible_facts', {})
        self.SETUP_CACHE[host].update(facts)
        self.SETUP_CACHE[host].update(self.extra_vars)
        if task.register:
            if 'stdout' in result:
                result['stdout_lines'] = result['stdout'].splitlines()
            self.SETUP_CACHE[host][task.register] = result
    if len(task.notify) > 0:
        for host, results in results.get('contacted', {}).iteritems():
            if results.get('changed', False):
                for handler_name in task.notify:
                    self._flag_handler(play, utils.template(play.basedir,
                        handler_name, task.module_vars), host)
    return hosts_remaining