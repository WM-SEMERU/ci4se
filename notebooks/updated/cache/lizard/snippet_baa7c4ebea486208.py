def save_workflow_to_cache(self, serialized_wf_instance):
    task_data = self.current.task_data.copy()
    for k, v in list(task_data.items()):
        if k.startswith('_'):
            del task_data[k]
    if 'cmd' in task_data:
        del task_data['cmd']
    self.wf_state.update({'step': serialized_wf_instance, 'data': task_data,
        'name': self.current.workflow_name, 'wf_id': self.workflow_spec.wf_id})
    if self.current.lane_id:
        self.current.pool[self.current.lane_id] = self.current.role.key
    self.wf_state['pool'] = self.current.pool
    self.current.log.debug('POOL Content before WF Save: %s' % self.current
        .pool)
    self.current.wf_cache.save(self.wf_state)