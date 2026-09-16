def task(self, func, *args, **kwargs):
    task = self.gator.task_class(**self.task_kwargs)
    return self.gator.push(task, func, *args, **kwargs)