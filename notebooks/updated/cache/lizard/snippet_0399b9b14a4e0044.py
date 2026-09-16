def _add_sub_tasks_to_executor(self, parent_task, parent_task_result):
    for sub_task in self.waiting_task_list.get_next_tasks(parent_task.id):
        self.executor.add_task(sub_task, parent_task_result)