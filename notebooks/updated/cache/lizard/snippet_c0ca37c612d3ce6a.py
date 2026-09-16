def task_assignments(self):
    url = str.format('projects/{}/task_assignments', self.id)
    response = self.hv.get_request(url)
    return [TaskAssignment(self.hv, tj['task_assignment']) for tj in response]