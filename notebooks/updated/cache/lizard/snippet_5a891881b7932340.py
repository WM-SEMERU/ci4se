def priority_run(self, hosts, function, attempts=1):
    return self._run(hosts, function, self.workqueue.priority_enqueue,
        False, attempts)