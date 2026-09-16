def parse_workflow_call(self, i):
    task_being_called = self.parse_workflow_call_taskname(i.attr('task'))
    task_alias = self.parse_workflow_call_taskalias(i.attr('alias'))
    io_map = self.parse_workflow_call_body(i.attr('body'))
    if not task_alias:
        task_alias = task_being_called
    return {'task': task_being_called, 'alias': task_alias, 'io': io_map}