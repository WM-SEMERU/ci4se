def delete_logtail_config(self, project_name, config_name):
    headers = {}
    params = {}
    resource = '/configs/' + config_name
    resp, headers = self._send('DELETE', project_name, None, resource,
        params, headers)
    return DeleteLogtailConfigResponse(headers, resp)