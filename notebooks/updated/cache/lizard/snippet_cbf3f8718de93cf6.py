def start_task(self, name, size):
    if len(self.task_stack) == 0:
        self.start_time = datetime.datetime.now()
    self.task_stack.append(Task(name, size, 0))