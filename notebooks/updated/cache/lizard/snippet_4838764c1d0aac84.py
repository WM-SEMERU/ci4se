def permissions(self):
    records = self.graph.get('me/permissions')['data']
    permissions = []
    for record in records:
        if record['status'] == 'granted':
            permissions.append(record['permission'])
    return permissions