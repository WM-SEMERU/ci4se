def schedule(self, seconds: float):

    def wrap(func: Callable):
        self._schedules.append(Scheduler(self.app, seconds, func))
    return wrap