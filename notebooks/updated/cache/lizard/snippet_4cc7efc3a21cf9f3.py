def describe(self, element):
    if element == 'tasks':
        return self.tasks_df.describe()
    elif element == 'task_runs':
        return self.task_runs_df.describe()
    else:
        return 'ERROR: %s not found' % element