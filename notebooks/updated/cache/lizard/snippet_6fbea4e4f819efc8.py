def remove_task(cls, task):
    with cls._lock:
        if not isinstance(task, Task):
            task = cls.resolved_task(task)
        if task:
            cls.tasks.remove(task)
        cls.tasks.sort()