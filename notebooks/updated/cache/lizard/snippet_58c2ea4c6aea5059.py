def delete_external_store(self, project_name, store_name):
    headers = {}
    params = {}
    resource = '/externalstores/' + store_name
    resp, header = self._send('DELETE', project_name, None, resource,
        params, headers)
    return DeleteExternalStoreResponse(header, resp)