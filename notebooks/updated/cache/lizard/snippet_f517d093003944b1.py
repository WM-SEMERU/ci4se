def count_buildable_tasks(self):
    self.update_tasks_status()
    buildable_tasks_count = 0
    for key, task in self.tasks.iteritems():
        if task.state is Task.State.NEW:
            if self.are_dependencies_buildable(task):
                buildable_tasks_count += 1
                logging.debug('Buildable task: %s' % task.name)
            else:
                logging.debug('Task %s has broken dependencies.' % task.name)
    return buildable_tasks_count