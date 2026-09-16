def find_deadlocks(self):
    runnables = []
    for work in self:
        runnables.extend(work.fetch_alltasks_to_run())
    runnables.extend(list(self.iflat_tasks(status=self.S_SUB)))
    running = list(self.iflat_tasks(status=self.S_RUN))
    err_tasks = self.errored_tasks
    deadlocked = []
    if err_tasks:
        for task in self.iflat_tasks():
            if any(task.depends_on(err_task) for err_task in err_tasks):
                deadlocked.append(task)
    return dict2namedtuple(deadlocked=deadlocked, runnables=runnables,
        running=running)