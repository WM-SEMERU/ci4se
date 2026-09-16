def addTask(self, task):
    task.initialize(self)
    task.start()
    with self._lock_c:
        self.numtasks += 1
        self.taskset.append(task)