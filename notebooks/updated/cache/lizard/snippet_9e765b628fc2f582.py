def get_machine_group_applied_configs(self, project_name, group_name):
    headers = {}
    params = {}
    resource = '/machinegroups/' + group_name + '/configs'
    resp, header = self._send('GET', project_name, None, resource, params,
        headers)
    return GetMachineGroupAppliedConfigResponse(resp, header)