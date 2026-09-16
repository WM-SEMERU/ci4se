def create_group(self, name):
    url = 'rest/api/2/group'
    data = {'name': name}
    return self.post(url, data=data)