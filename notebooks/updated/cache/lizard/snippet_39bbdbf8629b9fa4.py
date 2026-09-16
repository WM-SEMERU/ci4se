def stop_running_tasks(self):
    for task in self.__running_registry:
        task.stop()
    self.__running_registry.clear()