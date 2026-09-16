def pop(self):
    data = self.backend.pop(self.queue_name)
    if data:
        task = self.task_class.deserialize(data)
        return self.execute(task)