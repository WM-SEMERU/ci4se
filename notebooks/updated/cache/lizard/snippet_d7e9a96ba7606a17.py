def get_node_resource_by_type(api_url=None, node_name=None, type_name=None,
    verify=False, cert=list()):
    return utils._make_api_request(api_url, '/nodes/{0}/resources/{1}'.
        format(node_name, type_name), verify, cert)