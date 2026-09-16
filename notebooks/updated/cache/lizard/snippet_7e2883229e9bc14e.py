def add_task_status(self, name, **attrs):
    return TaskStatuses(self.requester).create(self.id, name, **attrs)