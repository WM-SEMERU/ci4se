def create_organization(self, name):
    log.warning('Creating organization...')
    url = 'rest/servicedeskapi/organization'
    data = {'name': name}
    return self.post(url, headers=self.experimental_headers, data=data)