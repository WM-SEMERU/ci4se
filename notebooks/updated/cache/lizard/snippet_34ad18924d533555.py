def _setup_cgroup_time_limit(self, hardtimelimit, softtimelimit,
    walltimelimit, cgroups, cores, pid_to_kill):
    cgroup_hardtimelimit = hardtimelimit if CPUACCT in cgroups else None
    if any([cgroup_hardtimelimit, softtimelimit, walltimelimit]):
        timelimitThread = _TimelimitThread(cgroups=cgroups, hardtimelimit=
            cgroup_hardtimelimit, softtimelimit=softtimelimit,
            walltimelimit=walltimelimit, pid_to_kill=pid_to_kill, cores=
            cores, callbackFn=self._set_termination_reason, kill_process_fn
            =self._kill_process)
        timelimitThread.start()
        return timelimitThread
    return None