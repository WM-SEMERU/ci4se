def createforkrelation(self, project_id, from_project_id):
    data = {'id': project_id, 'forked_from_id': from_project_id}
    request = requests.post('{0}/{1}/fork/{2}'.format(self.projects_url,
        project_id, from_project_id), headers=self.headers, data=data,
        verify=self.verify_ssl, auth=self.auth, timeout=self.timeout)
    if request.status_code == 201:
        return True
    else:
        return False