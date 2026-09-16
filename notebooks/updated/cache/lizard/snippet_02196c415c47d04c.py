def _polling_iteration(self):
    if self.__task is None:
        self.ready_event().set()
    elif self.__task.check_events() is True:
        self.ready_event().set()
        self.registry().task_finished(self)