def createbranch(self, project_id, branch, ref):
    data = {'id': project_id, 'branch_name': branch, 'ref': ref}
    request = requests.post('{0}/{1}/repository/branches'.format(self.
        projects_url, project_id), headers=self.headers, data=data, verify=
        self.verify_ssl, auth=self.auth, timeout=self.timeout)
    if request.status_code == 201:
        return request.json()
    else:
        return False