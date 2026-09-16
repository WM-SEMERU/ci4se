def __thread_started(self):
    if self.__task is None:
        raise RuntimeError('Unable to start thread without "start" method call'
            )
    self.__task.start()
    self.__task.start_event().wait(self.__scheduled_task_startup_timeout__)