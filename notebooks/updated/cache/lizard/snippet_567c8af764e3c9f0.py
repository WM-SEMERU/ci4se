def remove(self, task_cls):
    registry_tag = task_cls.__registry_tag__
    if registry_tag in self.__registry.keys():
        self.__registry[registry_tag] = list(filter(lambda x: x != task_cls,
            self.__registry[registry_tag]))
        if len(self.__registry[registry_tag]) == 0:
            self.__registry.pop(registry_tag)