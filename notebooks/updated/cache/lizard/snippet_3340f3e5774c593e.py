def new(namespace, name, protected=False, attributes=dict(), api_url=fapi.
    PROD_API_ROOT):
    r = fapi.create_workspace(namespace, name, protected, attributes, api_url)
    fapi._check_response_code(r, 201)
    return Workspace(namespace, name, api_url)