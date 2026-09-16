def from_task(cls, task):
    target = cls(name=task.get_name(), params=task.get_param_string())
    return target