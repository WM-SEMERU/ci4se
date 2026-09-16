def add(self, task_cls):
    registry_tag = task_cls.__registry_tag__
    if registry_tag not in self.__registry.keys():
        self.__registry[registry_tag] = [task_cls]
    elif self.__multiple_tasks_per_tag__ is True:
        self.__registry[registry_tag].append(task_cls)
    else:
        raise RuntimeError('Multiple tasks with same tag appended')