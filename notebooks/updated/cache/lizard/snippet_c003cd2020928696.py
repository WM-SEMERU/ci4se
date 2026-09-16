def group_members(self, group, limit=99999):
    url = 'rest/api/1.0/admin/groups/more-members'
    params = {}
    if limit:
        params['limit'] = limit
    if group:
        params['context'] = group
    return (self.get(url, params=params) or {}).get('values')