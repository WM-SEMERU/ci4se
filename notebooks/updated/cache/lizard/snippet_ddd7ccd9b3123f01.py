def build_api_url(project, method, base_url):
    return API_URL_TEMPLATE.format(api_base=base_url, api_version=
        API_VERSION, project=project, method=method)