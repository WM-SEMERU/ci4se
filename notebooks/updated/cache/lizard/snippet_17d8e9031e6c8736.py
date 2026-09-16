def task_runner_add(self, parent, item, command):
    parent_task_id = self.item_to_id.get(parent)
    task_id = self.task_runner.add(parent_task_id, command)
    self.item_to_id[item] = task_id