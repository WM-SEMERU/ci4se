def update_host_template(resource_root, name, cluster_name, api_host_template):
    return call(resource_root.put, HOST_TEMPLATE_PATH % (cluster_name, name
        ), ApiHostTemplate, data=api_host_template, api_version=3)