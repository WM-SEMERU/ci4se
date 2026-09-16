def get_organisational_tags_to_task(self):
    if self._organisational_tags_to_task != {}:
        return self._organisational_tags_to_task
    for taskid, task in self.get_tasks().items():
        for tag in task.get_tags()[2]:
            self._organisational_tags_to_task.setdefault(tag.get_name(), []
                ).append(taskid)
    return self._organisational_tags_to_task