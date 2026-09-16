def update_group(self, group_id, new_name):
    data = {'id': group_id, 'name': new_name}
    try:
        response = self.post('updateGroup', data)
    except Exception:
        pass
    response = self.post('loadGroups', {'groupId': group_id})[0]
    return _fix_group(response)