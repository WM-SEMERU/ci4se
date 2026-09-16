def add_task(self, pid):
    _register_process_with_cgrulesengd(pid)
    for cgroup in self.paths:
        with open(os.path.join(cgroup, 'tasks'), 'w') as tasksFile:
            tasksFile.write(str(pid))