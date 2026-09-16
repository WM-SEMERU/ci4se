def rq_task(self):
    task_path = self.task.split('.')
    module_name = '.'.join(task_path[:-1])
    task_name = task_path[-1]
    module = importlib.import_module(module_name)
    return getattr(module, task_name)