def get_all_roles(resource_root, service_name, cluster_name='default', view
    =None):
    return call(resource_root.get, _get_roles_path(cluster_name,
        service_name), ApiRole, True, params=view and dict(view=view) or None)