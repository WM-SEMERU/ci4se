def database_list_projects(object_id, input_params={}, always_retry=True,
    **kwargs):
    return DXHTTPRequest('/%s/listProjects' % object_id, input_params,
        always_retry=always_retry, **kwargs)