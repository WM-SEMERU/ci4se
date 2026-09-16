def update_workspace_attributes(namespace, workspace, attrs):
    headers = _fiss_agent_header({'Content-type': 'application/json'})
    uri = '{0}workspaces/{1}/{2}/updateAttributes'.format(fcconfig.root_url,
        namespace, workspace)
    body = json.dumps(attrs)
    return __SESSION.patch(uri, headers=headers, data=body)