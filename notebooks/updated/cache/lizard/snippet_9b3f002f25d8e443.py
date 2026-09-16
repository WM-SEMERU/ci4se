def stop_instances(self, instance_ids=None, force=False):
    params = {}
    if force:
        params['Force'] = 'true'
    if instance_ids:
        self.build_list_params(params, instance_ids, 'InstanceId')
    return self.get_list('StopInstances', params, [('item', Instance)],
        verb='POST')