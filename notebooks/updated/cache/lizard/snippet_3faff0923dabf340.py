def getmergerequest(self, project_id, mergerequest_id):
    request = requests.get('{0}/{1}/merge_request/{2}'.format(self.
        projects_url, project_id, mergerequest_id), headers=self.headers,
        verify=self.verify_ssl, auth=self.auth, timeout=self.timeout)
    if request.status_code == 200:
        return request.json()
    else:
        return False