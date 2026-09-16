def createproject(self, name, **kwargs):
    data = {'name': name}
    if kwargs:
        data.update(kwargs)
    request = requests.post(self.projects_url, headers=self.headers, data=
        data, verify=self.verify_ssl, auth=self.auth, timeout=self.timeout)
    if request.status_code == 201:
        return request.json()
    elif request.status_code == 403:
        if 'Your own projects limit is 0' in request.text:
            print(request.text)
            return False
    else:
        return False