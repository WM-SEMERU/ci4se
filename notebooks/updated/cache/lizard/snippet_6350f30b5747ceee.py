def tasks_by_tag(self, registry_tag):
    if registry_tag not in self.__registry.keys():
        return None
    tasks = self.__registry[registry_tag]
    return tasks if self.__multiple_tasks_per_tag__ is True else tasks[0]