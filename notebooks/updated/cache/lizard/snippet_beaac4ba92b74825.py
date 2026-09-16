def next(self, task):
    uuid = str(task.uuid)
    for idx, otask in enumerate(self.tasks[:-1]):
        if otask.uuid == uuid:
            if self.tasks[idx + 1].status != 'SUCCESS':
                return self.tasks[idx + 1]
            else:
                uuid = self.tasks[idx + 1].uuid