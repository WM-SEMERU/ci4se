def apply_config_to_machine_group(self, project_name, config_name, group_name):
    headers = {}
    params = {}
    resource = '/machinegroups/' + group_name + '/configs/' + config_name
    resp, header = self._send('PUT', project_name, None, resource, params,
        headers)
    return ApplyConfigToMachineGroupResponse(header, resp)