def get_finished_results(self):
    task_and_results = []
    for pending_result in self.pending_results:
        if pending_result.ready():
            ret = pending_result.get()
            task_id, result = ret
            task = self.task_id_to_task[task_id]
            self.process_all_messages_in_queue()
            task.after_run(result)
            task_and_results.append((task, result))
            self.pending_results.remove(pending_result)
    return task_and_results