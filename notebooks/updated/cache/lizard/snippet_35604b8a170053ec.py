def uninstall_task(self, name):
    if name in self._task_type_by_name:
        self._task_type_by_name[name].options_scope = None
        del self._task_type_by_name[name]
        self._ordered_task_names = [x for x in self._ordered_task_names if 
            x != name]
    else:
        raise GoalError('Cannot uninstall unknown task: {0}'.format(name))