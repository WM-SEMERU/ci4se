def editlabel(self, project_id, name, new_name=None, color=None):
    data = {'name': name, 'new_name': new_name, 'color': color}
    request = requests.put('{0}/{1}/labels'.format(self.projects_url,
        project_id), data=data, verify=self.verify_ssl, auth=self.auth,
        headers=self.headers, timeout=self.timeout)
    if request.status_code == 200:
        return request.json()
    else:
        return False