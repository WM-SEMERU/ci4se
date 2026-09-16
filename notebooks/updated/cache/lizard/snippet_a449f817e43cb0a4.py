def update_machine_group(self, project_name, group_detail):
    headers = {}
    params = {}
    resource = '/machinegroups/' + group_detail.group_name
    headers['Content-Type'] = 'application/json'
    body = six.b(json.dumps(group_detail.to_json()))
    headers['x-log-bodyrawsize'] = str(len(body))
    resp, headers = self._send('PUT', project_name, body, resource, params,
        headers)
    return UpdateMachineGroupResponse(headers, resp)