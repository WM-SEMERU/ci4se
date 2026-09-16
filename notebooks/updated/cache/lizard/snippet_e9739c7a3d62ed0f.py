def delete_logstore(self, project_name, logstore_name):
    headers = {}
    params = {}
    resource = '/logstores/' + logstore_name
    resp, header = self._send('DELETE', project_name, None, resource,
        params, headers)
    return DeleteLogStoreResponse(header, resp)