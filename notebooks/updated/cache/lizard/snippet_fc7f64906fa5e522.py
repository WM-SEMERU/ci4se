def creategroup(self, name, path, **kwargs):
    data = {'name': name, 'path': path}
    if kwargs:
        data.update(kwargs)
    request = requests.post(self.groups_url, data=data, headers=self.
        headers, verify=self.verify_ssl, auth=self.auth, timeout=self.timeout)
    if request.status_code == 201:
        return request.json()
    else:
        msg = request.json()['message']
        raise exceptions.HttpError(msg)