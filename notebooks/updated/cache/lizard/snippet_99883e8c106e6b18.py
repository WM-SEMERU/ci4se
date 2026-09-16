def run(self):
    is_lane_changed = False
    while self._should_we_run():
        self.check_for_rerun_user_task()
        task = None
        for task in self.workflow.get_tasks(state=Task.READY):
            self.current.old_lane = self.current.lane_name
            self.current._update_task(task)
            if self.catch_lane_change():
                return
            self.check_for_permission()
            self.check_for_lane_permission()
            self.log_wf_state()
            self.switch_lang()
            self.run_activity()
            self.parse_workflow_messages()
            self.workflow.complete_task_from_id(self.current.task.id)
            self._save_or_delete_workflow()
            self.switch_to_external_wf()
        if task is None:
            break
    self.switch_from_external_to_main_wf()
    self.current.output['token'] = self.current.token
    for task in self.workflow.get_tasks(state=Task.READY):
        self.current._update_task(task)
        self.catch_lane_change()
        self.handle_wf_finalization()