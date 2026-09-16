def start(self):
    while True:
        task = self.taskmaster.next_task()
        if task is None:
            break
        try:
            task.prepare()
            if task.needs_execute():
                task.execute()
        except:
            if self.interrupted():
                try:
                    raise SCons.Errors.BuildError(task.targets[0], errstr=
                        interrupt_msg)
                except:
                    task.exception_set()
            else:
                task.exception_set()
            task.failed()
        else:
            task.executed()
        task.postprocess()
    self.taskmaster.cleanup()