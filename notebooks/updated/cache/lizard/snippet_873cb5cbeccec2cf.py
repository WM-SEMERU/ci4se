def set_all_requested_intervals(self, requested_intervals):
    for workflow_id in self.workflows:
        if self.workflows[workflow_id].online:
            self.workflows[workflow_id
                ].requested_intervals = requested_intervals