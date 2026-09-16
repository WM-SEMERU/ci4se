def list_machine_group(self, project_name, offset=0, size=100):
    if int(size) == -1 or int(size) > MAX_LIST_PAGING_SIZE:
        return list_more(self.list_machine_group, int(offset), int(size),
            MAX_LIST_PAGING_SIZE, project_name)
    headers = {}
    params = {}
    resource = '/machinegroups'
    params['offset'] = str(offset)
    params['size'] = str(size)
    resp, header = self._send('GET', project_name, None, resource, params,
        headers)
    return ListMachineGroupResponse(resp, header)