def allocate(self, manager=None):
    for i, task in enumerate(self):
        if not hasattr(task, 'manager'):
            if manager is not None:
                task.set_manager(manager)
            elif hasattr(self, 'manager'):
                task.set_manager(self.manager)
            else:
                task.set_manager(self.flow.manager)
        task_workdir = os.path.join(self.workdir, 't' + str(i))
        if not hasattr(task, 'workdir'):
            task.set_workdir(task_workdir)
        elif task.workdir != task_workdir:
            raise ValueError('task.workdir != task_workdir: %s, %s' % (task
                .workdir, task_workdir))